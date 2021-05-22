# 
#                            VoiceDB class - 
# Creating an instance of this class will give access to 2 APIs
# 1. insertUser() - inserting a user with name and voiceit uid to voice auth database
# 2. getUser() - getting voiceit uid against a name from voice auth database
#

import datetime
import sys
import Database

db_name = 'voice-assistant'
collection_name = 'voice-auth'

class VoiceDB:

    def insertUser(name, uid):

        """
            Inserting a user with name and voiceit uid to voice auth database
        """
        
        # connection to our mongodb database
        client = Database.mongo_client()
        # reference to database defined by db_name
        db = client.get_database(db_name)

        # The document to be inserted
        # Python dictionary is json corresponding datastructure 
        # Ideal for us to create a dictionary and this will be inserted as json object in collection
        object_to_insert = {
                "timeStamp" : datetime.datetime.utcnow(),
                "name": name,
                "uid": uid
            }

        try:
            # reference to the particular connection
            collection = db[collection_name]
            # Pymongo insert call on the collection
            insert_id = collection.insert(object_to_insert)
            return insert_id
        except:
            print("exc:", sys.exc_info()) 
        

    def getUser(name):

        """
            Getting user id against a name from the voice-auth collection
        """
        
        # connection to our mongodb database
        client = Database.mongo_client()
        # reference to database defined by db_name
        db = client.get_database(db_name)

        try:
             # reference to the particular connection
            collection = db[collection_name]
            # Pymongo insert call on the collection
            # Will return the first matching document
            search = collection.find_one({"name":name})
            return search['uid'] 
        except:
            print("exc:", sys.exc_info()) 
