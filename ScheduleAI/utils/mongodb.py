import os
import sys
from pymongo.mongo_client import MongoClient

from ScheduleAI.logger import logging
from ScheduleAI.exception import ErrorException

class MongoDBOp:
    def __init__(self,MONGO_URL):
        try:
         self.Url=MONGO_URL
        except Exception as e:
           raise ErrorException(e,sys)
    def InsertMany(self,):
        