import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

# Initialize Flask
app = Flask(__name__)
CORS(app)

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Global variables (will be initialized later)
LLM = None
vector_store = None
rag_chain = None

# Import prompt template
from ScheduleAI.utils.prompt_temp import system_prompt

# Function to initialize heavy models and chain
def initialize_models():
    global LLM, vector_store, rag_chain

    # Import heavy modules here to avoid slowing server startup
    from langchain.chat_models import init_chat_model
    from langchain_community.embeddings import HuggingFaceEmbeddings
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.runnables import RunnablePassthrough
    from langchain_pinecone import PineconeVectorStore

    print("Initializing LLM, embeddings, and Pinecone vector store...")

    # Initialize LLM
    LLM = init_chat_model(
        "google_genai:gemini-2.5-flash-lite",
        google_api_key=GEMINI_API_KEY
    )

    # Initialize embeddings
    model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )

    # Connect to existing Pinecone index
    index_name = "scheduleai-index"
    vector_store = PineconeVectorStore.from_existing_index(
        index_name=index_name,
        embedding=model
    )

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    # Build prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{user_input}")
    ])

    # Build RAG chain
    rag_chain = (
        {
            "context": retriever | (lambda docs: "\n\n".join(d.page_content for d in docs)),
            "user_input": RunnablePassthrough(),
        }
        | prompt
        | LLM
    )

    print("Models initialized successfully!")


# Route for homepage
@app.route('/')
def home():
    return render_template('index.html')


# Chat route
@app.route('/chat', methods=['POST'])
def chat():
    global rag_chain
    # Lazy initialization
    if rag_chain is None:
        initialize_models()

    user_msg = request.json.get("message")
    if not user_msg:
        return jsonify({"reply": "No message received!"})

    # Invoke RAG chain
    response = rag_chain.invoke(user_msg)
    return jsonify({"reply": response.content})


if __name__ == "__main__":
    # Flask server starts instantly
    app.run(host="0.0.0.0", port=5000, debug=True)
