"""Helpers for CSFLE implementation."""

import base64

from pymongo import MongoClient
import pymongocrypt
from pymongo.encryption_options import AutoEncryptionOpts
from pymongo.encryption import ClientEncryption
from bson.codec_options import CodecOptions
from bson.binary import Binary, STANDARD, UUID_SUBTYPE
from uuid import UUID

# Reading master key from the disk
def read_master_key(path="./master-key.txt"):
    with open(path, "rb") as f:
        return f.read(96)


class CsfleHelper:
    """This is a helper class that aids in csfle implementation."""

    def __init__(self,
                 kms_provider=None,
                 kms_provider_name="local",
                 key_alt_name="demo-data-key",
                 key_db="encryption",
                 key_coll="__keyVault",
                 master_key=None,
                 connection_string="mongodb+srv://nshept:nshept123@cluster0.ampjh.mongodb.net/voice-assistant?retryWrites=true&w=majority" ):
        """
        If mongocryptd is not installed to in your search path, ensure
        you override mongocryptd_spawn_path
        """
        super().__init__()
        if kms_provider is None:
            raise ValueError("kms_provider is required")
        self.kms_provider = kms_provider
        self.kms_provider_name = kms_provider_name
        self.key_alt_name = key_alt_name
        self.key_db = key_db
        self.key_coll = key_coll
        self.master_key = master_key
        self.key_vault_namespace = f"{self.key_db}.{self.key_coll}"
        self.connection_string = connection_string
        
    def key_from_base64(base64_key):
        return Binary(base64.b64decode(base64_key), UUID_SUBTYPE)

    def ensure_unique_index_on_key_vault(self, key_vault):
        # clients are required to create a unique partial index on keyAltNames
        key_vault.create_index("keyAltNames",
                               unique=True,
                               partialFilterExpression={
                                   "keyAltNames": {
                                       "$exists": True
                                   }
                               })
    # Method to find or create data key from master key
    def find_or_create_data_key(self):
        key_vault_client = MongoClient(self.connection_string)

        key_vault = key_vault_client[self.key_db][self.key_coll]

        self.ensure_unique_index_on_key_vault(key_vault)

        data_key = key_vault.find_one({"keyAltNames": self.key_alt_name})

        # create a key
        if data_key is None:
            with ClientEncryption(self.kms_provider,
                                  self.key_vault_namespace,
                                  key_vault_client,
                                  CodecOptions(uuid_representation=STANDARD)
                                  ) as client_encryption:

                # create data key using KMS master key
                return client_encryption.create_data_key(
                    self.kms_provider_name,
                    key_alt_names=[self.key_alt_name],
                    master_key=self.master_key)

        return data_key['_id'].bytes

    # Normal client
    def get_regular_client(self):
        return MongoClient(self.connection_string)

    # Encrypted Client
    def get_csfle_enabled_client(self):
        return MongoClient(
            self.connection_string,
            auto_encryption_opts=AutoEncryptionOpts(
                self.kms_provider,
                self.key_vault_namespace,
                bypass_auto_encryption=True)
        )

    