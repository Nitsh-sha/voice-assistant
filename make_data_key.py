"""This file finds and prints or makes and prints a data key used for
encrpytion."""

import base64
from uuid import UUID
from helpers import read_master_key, CsfleHelper


def main():

    local_master_key = read_master_key()

    kms_provider = {
        "local": {
            "key": local_master_key,
        },
    }

    csfle_helper = CsfleHelper(kms_provider=kms_provider)
    binary_data_key = csfle_helper.find_or_create_data_key()
    data_key = base64.b64encode(binary_data_key).decode("utf-8")

    print("Base64 data key. Copy and paste this into app.py\t", data_key)


if __name__ == "__main__":
    main()
