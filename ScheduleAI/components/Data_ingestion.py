import os,sys,json
from ScheduleAI.logger import logging
from ScheduleAI.utils.mongodb import MongoDBOp
from ScheduleAI.exception import ErrorException
from datetime import datetime
from dataclasses import dataclass
TIMESTAMP:str=datetime.now.strftime("%m_%d_%Y_%H_%M_%S")
@dataclass
class Artifact:
 artifactdir=os.path.join("artifact",TIMESTAMP)

artifactConfig:Artifact=Artifact()


class DataIngestionConfig:
 dataingestionDir:str=os.path.join(artifactConfig.artifactdir,"Dataingestion")
 instruction_file:str=os.path.join(dataingestionDir,"instruction.json")
 preference_file:str=os.path.join(dataingestionDir,"preference.json")
 raw_file:str=os.path.join(dataingestionDir,"preference.json")


class DataIngestion:
 def __init__(self,MONGO_URL):
  self.URL=MONGO_URL
  self.COLLECTION_ARR=["Instruction","","Prefrence","rawdata"]
 def initiate_data_ingestion(self,):
  try:
   logging.info("entered data ingestion initiation")
   for collection in self.COLLECTION_ARR:
    logging.info(f"fetching data from collection:{collection}")
    mongodb=MongoDBOp(MONGO_URL=self.URL,DB_NAME="AiScheduler")
    if collection=="Instruction":
      instruction_data=list(mongodb.FetchALL(collection))
      with open(DataIngestionConfig.instruction_file,"w") as f:
        json.dump(instruction_data,f,indent=4)
    if collection=="Preference":
      preference_data=list(mongodb.FetchALL(collection))
      with open(DataIngestionConfig.preference_file,"w") as f:
        json.dump(preference_data,f,indent=4)
    if collection=="rawdata":
      raw_data=list(mongodb.FetchALL(collection))
      with open(DataIngestionConfig.raw_file,"w") as f:
        json.dump(raw_data,f,indent=4)
    logging.info(f"data ingestion completed for collection:{collection}")
   logging.info("data ingestion completed")

  except Exception as e:
   raise ErrorException(e,sys)
