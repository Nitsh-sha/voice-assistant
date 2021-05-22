from collections import OrderedDict
import sys
import Database

db_name = 'voice-assistant'

# Defining various schemas for corresponding collections in our database. 
# MongoDB is non-relational database and is collections/documents based which is 
# very differenet from relational databases where there are tables and fields
# In our case, documents not need to have to any fixed schema
# It is entirely upto us to enforce schema on the collection
# In below schemas, we are just ensuring that each document should have atleast required fields

SearchHistorySchema = {"$jsonSchema":
        {
         "bsonType": "object",
         "required": [ "timeStamp", "keyword","description" ],
         "properties": 
            {
                "timeStamp":
                  {
                    "bsonType": "date",
                    "description": "must be a datetime object and is required"
                  },
                "keyword": 
                  {
                    "bsonType": "string",
                    "description": "must be a string and is required required"
                  },
                "description": 
                  {
                    "bsonType": "string",
                    "description": "must be a string and is required required"
                  }
            }
        }
    }
WebHistorySchema = {"$jsonSchema":
        {
         "bsonType": "object",
         "required": [ "timeStamp", "keyword" ],
         "properties": 
            {
                "timeStamp":
                  {
                    "bsonType": "date",
                    "description": "must be a datetime object and is required"
                  },
                "keyword": 
                  {
                    "bsonType": "string",
                    "description": "must be a string and is required required"
                  }
            }
        }
    }
NewsHistorySchema = {"$jsonSchema":
        {
         "bsonType": "object",
         "required": [ "timeStamp", "keyword" ],
         "properties": 
            {
                "timeStamp":
                  {
                    "bsonType": "date",
                    "description": "must be a datetime object and is required"
                  },
                "keyword": 
                  {
                    "bsonType": "string",
                    "description": "must be a string and is required required"
                  }
            }
        }
    }

YoutubeHistorySchema = {"$jsonSchema":
        {
         "bsonType": "object",
         "required": [ "timeStamp", "keyword", "count" ],
         "properties": 
            {
                "timeStamp":
                  {
                    "bsonType": "date",
                    "description": "must be a datetime object and is required"
                  },
                "keyword": 
                  {
                    "bsonType": "string",
                    "description": "must be a string and is required required"
                  },
                "count": 
                {
                  "bsonType": "int",
                  "description": "must be an integer and is required required"
                }
            }
        }
    }

WikiHistorySchema = {"$jsonSchema":
        {
         "bsonType": "object",
         "required": [ "timeStamp", "keyword","description" ],
         "properties": 
            {
                "timeStamp":
                  {
                    "bsonType": "date",
                    "description": "must be a datetime object and is required"
                  },
                "keyword": 
                  {
                    "bsonType": "string",
                    "description": "must be a string and is required required"
                  },
                "description": 
                  {
                    "bsonType": "string",
                    "description": "must be a string and is required required"
                  }
            }
        }
    }


VoiceAuthSchema = {"$jsonSchema":
        {
         "bsonType": "object",
         "required": [ "timeStamp", "name","uid" ],
         "properties": 
            {
                "timeStamp":
                  {
                    "bsonType": "date",
                    "description": "must be a datetime object and is required"
                  },
                "name": 
                  {
                    "bsonType": "string",
                    "description": "must be a string and is required required"
                  },
                "uid": 
                  {
                    "bsonType": "string",
                    "description": "must be a string and is required required"
                  }
            }
        }
    }

EmailSchema = {"$jsonSchema":
        {
         "bsonType": "object",
         "required": [ "timeStamp", "sender", "reciever", "subject", "content" ],
         "properties": 
            {
                "timeStamp":
                  {
                    "bsonType": "date",
                    "description": "must be a datetime object and is required"
                  },
                "sender": 
                  {
                    "bsonType": "string",
                    "description": "must be a string and is required required"
                  },
                "reciever": 
                  {
                    "bsonType": "string",
                    "description": "must be a string and is required required"
                  },
                 "subject": 
                  {
                    "bsonType": "string",
                    "description": "must be a string and is required required"
                  },    
                "content": 
                  {
                    "bsonType": "string",
                    "description": "must be a string and is required required"
                  }
            }
        }
    }

MessageSchema = {"$jsonSchema":
        {
         "bsonType": "object",
         "required": [ "timeStamp", "reciever", "number", "content" ],
         "properties": 
            {
                "timeStamp":
                  {
                    "bsonType": "date",
                    "description": "must be a datetime object and is required"
                  },
                "reciever": 
                  {
                    "bsonType": "string",
                    "description": "must be a string and is required required"
                  },
                "number": 
                  {
                    "bsonType": "string",
                    "description": "must be a string and is required required"
                  },
                "content": 
                  {
                    "bsonType": "string",
                    "description": "must be a string and is required required"
                  }   
            }
        }
    }


NotesSchema = {"$jsonSchema":
        {
         "bsonType": "object",
         "required": [ "timeStamp", "title", "todo", "content" ],
         "properties": 
            {
                "timeStamp":
                  {
                    "bsonType": "date",
                    "description": "must be a datetime object and is required"
                  },
                "title": 
                  {
                    "bsonType": "string",
                    "description": "must be a string and is required required"
                  },
                "todo": 
                  {
                    "bsonType": "bool",
                    "description": "must be a true/false and is required required"
                  },  
                "content": 
                  {
                    "bsonType": "string",
                    "description": "must be a string and is required required"
                  }
            }
        }
    }

WeatherSchema = {"$jsonSchema":
        {
         "bsonType": "object",
         "required": [ "timeStamp", "weather", "desc", "temp", "location" ],
         "properties": 
            {
                "timeStamp":
                  {
                    "bsonType": "date",
                    "description": "must be a datetime object and is required"
                  },
                "weather": 
                  {
                    "bsonType": "string",
                    "description": "must be a string and is required required"
                  },
                "desc": 
                  {
                    "bsonType": "string",
                    "description": "must be a string and is required required"
                  },
                "temp": 
                  {
                    "bsonType": "double",
                    "description": "must be a string and is required required"
                  },    
                "location": 
                  {
                    "bsonType": "string",
                    "description": "must be a string and is required required"
                  }
            }
        }
    }

schema_dict = {
    'wiki-history': WikiHistorySchema,
    'search-history': SearchHistorySchema,
    'web-history': WebHistorySchema,
    'news-history': NewsHistorySchema,
    'youtube-history': YoutubeHistorySchema,
    'voice-auth' : VoiceAuthSchema,
    'email': EmailSchema,
    'message': MessageSchema,
    'notes': NotesSchema,
    'weather': WeatherSchema
}

def implementSchematoDB():

    #
    # Enforcing schema to the databse collections
    #
    client = Database.mongo_client()
    db = client.get_database(db_name)
    
    # List of collection on which we are setting auto expiration
    auto_expire_collections = ['wiki-history', 'web-history', 'search-history', 'news-history', 'youtube-history', 'weather']
    
    for name in schema_dict.keys():
      if name in auto_expire_collections:
        collection = db[name]
        collection.create_index("timeStamp", expireAfterSeconds = 30*24*60*60)
      cmd = OrderedDict([('collMod', name),
      ('validator', schema_dict[name]),
      ('validationLevel', 'moderate')])
      db.command(cmd)

if __name__ == "__main__":
  implementSchematoDB()
