import os
from ScheduleAI.components.Data_ingestion import DataIngestion
from dotenv import load_dotenv

load_dotenv()
URL=os.getenv("MONGODB_URL")
data_ingestion=DataIngestion(MONGO_URL=URL)
data_ingestion.initiate_data_ingestion()