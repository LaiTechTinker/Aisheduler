import os
import json
from dotenv import load_dotenv
from ScheduleAI.utils.mongodb import MongoDBOp
load_dotenv()
obj= {
                    "instruction": "Explain how an LLM Twin can enhance communication efficiency.",
                    "answer": "An LLM Twin enhances communication efficiency by automating responses and generating content that aligns with the user's established voice. This capability not only saves time but also ensures that the quality and tone of communication remain consistent. As a result, individuals can focus on more strategic tasks while the LLM Twin manages routine interactions, thus streamlining their overall workflow."
}
MONGO_URL=os.getenv("MONGODB_URL")
DB_NAME=os.getenv("DB_NAME")
file_path="./new_preference.json"
with open(file_path,"r") as f:
    data=json.load(f)
mongoClass=MongoDBOp(MONGO_URL, DB_NAME)
mongoClass.InsertMany("Prefrence",data)