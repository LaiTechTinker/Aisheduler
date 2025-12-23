import os
import json
from dotenv import load_dotenv
from ScheduleAI.utils.mongodb import MongoDBOp
load_dotenv()
MONGO_URL=os.getenv("MONGODB_URL")
DB_NAME=os.getenv("DB_NAME")
file_path="./new_instruct.json"
with open(file_path,"r") as f:
    data=json.load(f)
mongoClass=MongoDBOp(MONGO_URL, DB_NAME)
mongoClass.InsertMany("Instruction", data)