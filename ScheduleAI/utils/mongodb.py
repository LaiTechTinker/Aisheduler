import os
import sys
from pymongo.mongo_client import MongoClient

from ScheduleAI.logger import logging
from ScheduleAI.exception import ErrorException

class MongoDBOp:
    def __init__(self,MONGO_URL,DB_NAME):
        try:
         logging.info("entered the mongodb operation section")
         self.Client=MongoClient(MONGO_URL)
         self.database=self.Client[DB_NAME]
        except Exception as e:
           raise ErrorException(e,sys)
    def InsertMany(self,COLLECTION_NAME,Data):
     try:
       logging.info(f"entered the insertion of data from collection:{COLLECTION_NAME}")
       inserted_data=self.database[COLLECTION_NAME].insert_many(Data)
       return inserted_data
     except Exception as e:
        raise ErrorException(e,sys)
    def FetchALL(self,COLLECTION_NAME):
     try:
       logging.info(f"entered the fetching of data from collection:{COLLECTION_NAME}")
       returned_data=list(self.database[COLLECTION_NAME].find())
     except Exception as e:
       raise ErrorException(e,sys)
    def insertOne(self,COLLECTION_NAME,obj):
       try:
         logging.info("entered the single insertion of obj stage")
         collection=self.database[COLLECTION_NAME]
         collection.insert_one(obj)
         logging.info("insertion successfully")
       except Exception as e:
         raise ErrorException(e,sys)
     