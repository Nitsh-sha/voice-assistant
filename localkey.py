import os
path = "master-key.txt"

# Generation of Master key and writing the key to a file on the disk
# for future reference
# Master key ideally should be stored with some KMS provider like AWS KMS or GCP KMS
# Master key should not be stored on browser side
# In our case, storing master key on our local disk is enough
# This method will create a random key of 12 bytes and save it on the disk
def generateMasterKey():    
    file_bytes = os.urandom(96)
    with open(path, "wb") as f:
        f.write(file_bytes)

# Method to read master key from the disk
def getMasterKey():    
    path = "./master-key.txt"
    with open(path, "rb") as f:
        local_master_key = f.read()
    print(local_master_key)
    return local_master_key


if __name__ == "__main__":
    generateMasterKey()