import os,sys
from ScheduleAI.logger import logging
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

