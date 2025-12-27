import os
from dotenv import load_dotenv
import langchain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.runnables import RunnablePassthrough
from langchain_pinecone import PineconeVectorStore
from langchain.chat_models import init_chat_model
from ScheduleAI.utils.prompt_temp import system_prompt
load_dotenv()
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
LLM= init_chat_model("google_genai:gemini-2.5-flash-lite",google_api_key=GEMINI_API_KEY)
index_name="scheduleai-index"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{user_input}")
    ]
)
model=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},      # or "cuda" if GPU available
    encode_kwargs={"normalize_embeddings": True}
)

vector_store=PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=model
)
retriever=vector_store.as_retriever(search_type="similarity",search_kwargs={"k":3})
rag_chain = (
    {
        "context": retriever | (lambda docs: "\n\n".join(d.page_content for d in docs)),
        "user_input": RunnablePassthrough(),
    }
    | prompt
    |LLM
)
