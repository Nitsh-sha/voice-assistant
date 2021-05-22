import datetime
import sys
import Database
from pprint import pprint

# Voice Assistant Database name
db_name = 'voice-assistant'

# Collection names
wiki_collection_name = 'wiki-history'
web_collection_name = 'web-history'
search_collection_name = 'search-history'
youtube_collection_name = 'youtube-history'
news_collection_name = 'news-history'


# Database insert/read methods

def addWikiHistory(search_tag, description):
    
    """
        Method to insert wiki search into 'wiki-history' collection
    """

    # A mongo client
    client = Database.mongo_client()
    # Connection to database specified by db_name
    db = client.get_database(db_name)

    # Object to insert
    # Python dictionary
    object_to_insert = {
            "keyword" : search_tag,
            "description": description,
            "timeStamp": datetime.datetime.utcnow()
        }

    try:
        # Collection in database in which insert_one() is called
        collection = db[wiki_collection_name]
        insert_id = collection.insert_one(object_to_insert)
        return insert_id
    except:
        print("exc:", sys.exc_info()) 
        

def getWikiHisotry():
    
    """
        Method to return most recent entry in the collection
        You can change the limit to specify the number of entries you want to retrieve        
    """
    # Mongoclient and connection to database specified by db_name
    client = Database.mongo_client()
    db = client.get_database(db_name)

    try:
        # Collection in database from which we make query
        collection = db[wiki_collection_name]
        # Returning a list of 3 most recent entries 
        search = list(collection.find().sort('timeStamp', -1).limit(3))
        pprint(search)
        return search
    except:
        print("exc:", sys.exc_info())



def addSearchHistory(search_tag, description):

    """
        Method to insert web search history into 'search-history' collection
    """
    # Object to insert
    # Python dictionary
    object_to_insert = {
            "timeStamp": datetime.datetime.utcnow(),
            "keyword" : search_tag,
            "description": description
        }
    
    # A mongo client
    client = Database.mongo_client()
    # Connection to database specified by db_name
    db = client.get_database(db_name)
    
    try:
        # Collection in database in which insert_one() is called
        collection = db[search_collection_name]
        insert_id = collection.insert_one(object_to_insert)
        return insert_id
    except:
        print("exc:", sys.exc_info()) 
    

def getSearchHisotry():
    
    """
        Method to return most recent entry in the collection
        You can change the limit to specify the number of entries you want to retrieve        
    """
    
    # search tag will define the query
    client = Database.mongo_client()
    db = client.get_database(db_name)
    
    try:
        # Collection in database from which we make query
        collection = db[search_collection_name]
        # Returning a list of 3 most recent entries 
        search = list(collection.find().sort('timeStamp', -1).limit(3))
        pprint(search)
        return search
    except:
        print("exc:", sys.exc_info())       



def addWebHistory(search_tag):

    """
        Method to insert website search into 'web-history' collection 
    """

    object_to_insert = {
            "timeStamp": datetime.datetime.utcnow(),
            "keyword" : search_tag
        }
    
    # A mongo client
    client = Database.mongo_client()
    # Connection to database specified by db_name
    db = client.get_database(db_name)
    
    try:
        collection = db[web_collection_name]
        insert_id = collection.insert_one(object_to_insert)
        return insert_id
    except:
        print("exc:", sys.exc_info()) 
    

def getWebHisotry():
    
    """
        Method to return most recent entry in the collection
        You can change the limit to specify the number of entries you want to retrieve
    """

    # A mongo client
    client = Database.mongo_client()
    # Connection to database specified by db_name
    db = client.get_database(db_name)
    
    try:
        collection = db[web_collection_name]
        # Returning a list of 3 most recent entries 
        search = list(collection.find().sort('timeStamp', -1).limit(3))
        pprint(search)
        return search
    except:
        print("exc:", sys.exc_info()) 


def addNewsHistory(search_tag):

    """
        # Method to insert news search history into 'news-history' collection
        You can change the limit to specify the number of entries you want to retrieve
    """ 
    
    object_to_insert = {
            "timeStamp": datetime.datetime.utcnow(),
            "keyword" : search_tag
        }
    
    # A mongo client
    client = Database.mongo_client()
    # Connection to database specified by db_name
    db = client.get_database(db_name)
    
    try:
        collection = db[news_collection_name]
        insert_id = collection.insert_one(object_to_insert)
        return insert_id
    except:
        print("exc:", sys.exc_info()) 
    

def getNewsHisotry():

    """
        Method to return most recent entry in the collection
        You can change the limit to specify the number of entries you want to retrieve
    """
    
    # A mongo client
    client = Database.mongo_client()
    # Connection to database specified by db_name
    db = client.get_database(db_name)
    
    try:
        collection = db[news_collection_name]
        # Returning a list of 3 most recent entries 
        search = list(collection.find().sort('timeStamp', -1).limit(3))
        pprint(search)
        return search
    except:
        print("exc:", sys.exc_info())


def addYoutubeHistory(video):
    
    """
        Method to insert youtube search into 'youtube-history' collection 
    """
    # A mongo client
    client = Database.mongo_client()
    # Connection to database specified by db_name
    db = client.get_database(db_name)

    try:
        collection = db[youtube_collection_name]
        # Looking if video is already in the database
        search = collection.find_one({"keyword":video})
        pprint(search)

        if search == None:
            # New video, not present in collection
            # Inserting the video with count as 1
            object_to_insert = {
            "timeStamp": datetime.datetime.utcnow(),
            "keyword" : video,
            "count" : 1
            }
            try:
                insert_id = collection.insert_one(object_to_insert)
                return insert_id
            except:
                print("exc:", sys.exc_info())
        else:
            # Video is already present in the collection
            # Increment the count by 1
            try:
                insert_id = collection.update_one({"keyword":video},{ '$inc': { 'count': 1 }})
                return insert_id
            except:
                print("exc:", sys.exc_info())
    except:
        print("exc:", sys.exc_info())
    

def getYoutubeFav():
    
    """
        Method to return list of videos which are played more than 3 times
        Favourites
        Change '$gte' and '$lt' values to modify the search
        PS - You can vary the number of elements to include by specifying the limit 
    """

    # A mongo client
    client = Database.mongo_client()
    # Connection to database specified by db_name
    db = client.get_database(db_name)

    try:
        # Collection in database from which we make query
        collection = db[youtube_collection_name]
        # List of first 5 documents where count is between 3 to 10
        search = list(collection.find({'count': {'$gte':3, '$lt': 10}}).limit(5))
        pprint(search)
        return search
    except:
        print("exc:", sys.exc_info())

# if __name__ == "__main__":
#     addNewsHistory("Farmers")
#     addWikiHistory("Aa", "aaa")