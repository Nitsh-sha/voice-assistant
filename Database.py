import pymongo

local_url = 'mongodb://localhost:27017/'
connection_url = "mongodb+srv://nshept:nshept123@cluster0.ampjh.mongodb.net/voice-assistant?retryWrites=true&w=majority"

def mongo_client():
    
    """
        This method will return a MongoClient object for our Cluster 
    """
    # connection/client to the mongo cluster specified with connection url
    client = pymongo.MongoClient(connection_url)
    return client

