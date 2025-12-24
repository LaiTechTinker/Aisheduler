import os,sys
from pinecone import ServerlessSpec,Pinecone
from langchain.vectorstores import Pinecone
from dotenv import load_dotenv
from ScheduleAI.logger import logging
from ScheduleAI.exception import ErrorException
from ScheduleAI.components.embedding import Embedding
load_dotenv()
PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
class Embeddingupload:
    def __init__(self,embedding):
        self.embedding=embedding
        self.pc=Pinecone(api_key=PINECONE_API_KEY)
        self.index_name="scheduleai-index"
    def create_index(self):
        try:
            logging.info("Creating Pinecone index")
            if self.index_name not in self.pc.list_indexes():
                self.pc.create_index(
                    name=self.index_name,
                    dimension=384,
                    metric="cosine",
                    spec=ServerlessSpec(cloud="aws",region="us-east-1")
                )
                logging.info("Index created successfully")
            else:
                logging.info("Index already exists")
            index=self.pc.index(self.index_name)
        except Exception as e:
            raise ErrorException(e,sys)
    def upload_embeddings(self):
        try:
            logging.info("Uploading embeddings to Pinecone index")
            index=self.pc.index(self.index_name)
            vectors=[(str(i),emb,None) for i,emb in enumerate(self.embedding)]
            index.upsert(vectors=vectors)
            logging.info("Embeddings uploaded successfully")
        except Exception as e:
            raise ErrorException(e,sys)


