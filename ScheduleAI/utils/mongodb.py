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
         logging.info("connected to mongodb successfully")
        except Exception as e:
           raise ErrorException(e,sys)
    def InsertMany(self,COLLECTION_NAME,Data):
     try:
       logging.info(f"entered the insertion of data from collection:{COLLECTION_NAME}")
       if isinstance(Data,dict) or isinstance(Data,list):
        inserted_data=self.database[COLLECTION_NAME].insert_many(Data)
        logging.info("data inserted successfully")
        return inserted_data
       else:
        logging.info("data is not in dict format")
        raise ValueError("data is not in dict format")
       return
     except Exception as e:
        raise ErrorException(e,sys)
    def FetchALL(self,COLLECTION_NAME):
     try:
       logging.info(f"entered the fetching of data from collection:{COLLECTION_NAME}")
       returned_data=self.database[COLLECTION_NAME].find()
       return returned_data
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
    def findOne(self,COLLECTION_NAME,id):
      try:
        logging.info("entered the single insertion of obj stage")
        collection=self.database[COLLECTION_NAME]
        find_data=collection.find_one(id)
        logging.info("insertion successfully")
        return find_data
        
      except Exception as e:
        raise ErrorException(e,sys)
    

     