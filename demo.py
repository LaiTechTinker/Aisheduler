from ScheduleAI.components.Data_ingestion import DataIngestion
from dotenv import load_dotenv
import os
load_dotenv()
URL=os.getenv("MONGO_URL")
data_ingestion=DataIngestion(MONGO_URL=URL)
data_ingestion.initiate_data_ingestion()