import os,sys,json
from ScheduleAI.logger import logging
from ScheduleAI.utils.mongodb import MongoDBOp
from ScheduleAI.exception import ErrorException
from datetime import datetime
from dataclasses import dataclass
TIMESTAMP:str=datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
@dataclass
class Artifact:
 artifactdir=os.path.join("artifact",TIMESTAMP)

artifactConfig:Artifact=Artifact()


class DataIngestionConfig:
 dataingestionDir:str=os.path.join(artifactConfig.artifactdir,"Dataingestion")
 instruction_file:str=os.path.join(dataingestionDir,"instruction.json")
 preference_file:str=os.path.join(dataingestionDir,"preference.json")
 raw_file:str=os.path.join(dataingestionDir,"rawdata.json")


class DataIngestion:
 def __init__(self,MONGO_URL):
  self.URL=MONGO_URL
  self.COLLECTION_ARR=["Instruction","","Prefrence","rawdata"]
  self.client=MongoDBOp(MONGO_URL=self.URL,DB_NAME="AiScheduler")
 def remove_id_field(self,data):
  try:
   for record in data:
    if '_id' in record:
     del record['_id']
   return data
  except Exception as e:
   raise ErrorException(e,sys)
 def initiate_data_ingestion(self,):
  try:
   os.makedirs(DataIngestionConfig.dataingestionDir,exist_ok=True)
   logging.info("entered data ingestion initiation")
   for collection in self.COLLECTION_ARR:
    logging.info(f"fetching data from collection:{collection}")
    if collection=="Instruction":
      instruction_data=list(self.client.FetchALL(collection))
      instruction_data=self.remove_id_field(instruction_data)
      with open(DataIngestionConfig.instruction_file,"w") as f:
        json.dump(instruction_data,f,indent=4)
    if collection=="Prefrence":
      preference_data=list(self.client.FetchALL(collection))
      preference_data=self.remove_id_field(preference_data)
      with open(DataIngestionConfig.preference_file,"w") as f:
        json.dump(preference_data,f,indent=4)
    if collection=="rawdata":
      raw_data=list(self.client.FetchALL(collection))
      raw_data=self.remove_id_field(raw_data)
      with open(DataIngestionConfig.raw_file,"w") as f:
        json.dump(raw_data,f,indent=4)
    logging.info(f"data ingestion completed for collection:{collection}")
   logging.info("data ingestion completed")

  except Exception as e:
   raise ErrorException(e,sys)
