import os
import sys
from ScheduleAI.logger import logging
from ScheduleAI.exception import ErrorException
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
class Embedding:
    def __init__(self,data):
        self.data=data
        self.model= HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},      # or "cuda" if GPU available
    encode_kwargs={"normalize_embeddings": True}
)
    def document_loader(self):
        try:
            logging.info("Loading documents loading")
            documents=[Document(
                page_content=data["answer"],metadata={"instruction":data["instruction"]}) for data in self.data]
            return documents
        except Exception as e:
            raise ErrorException(e,sys)
    def splitter(self,):
        try:
            logging.info("Splitting the documents")
            splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20, add_start_index=True)
            splitted_doc=splitter.split_documents(self.document_loader())
            return splitted_doc
        except Exception as e:
            raise ErrorException(e,sys)
    def create_embeddings(self,embedding_model):
        try:
            logging.info("creating embeddings for the documents")
          
            model=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},      # or "cuda" if GPU available
    encode_kwargs={"normalize_embeddings": True})
            Embedding=model.embed_documents(self.splitter())
            return Embedding
        except Exception as e:
            raise ErrorException(e,sys)
    