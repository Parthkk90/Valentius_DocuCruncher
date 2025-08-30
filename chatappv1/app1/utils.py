from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
import google.generativeai as genai
import os
import logging
logging.basicConfig(level=logging.INFO)
# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_pdf_text(pdf_paths):
    """Extract text from PDF files."""
    text = ""
    for pdf_path in pdf_paths:
        pdf_reader = PdfReader(pdf_path)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    """Split text into manageable chunks."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return text_splitter.split_text(text)

def get_vector_store(text_chunks):
    """Create and save the FAISS index."""
    try:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
        vector_store.save_local("faiss_index")
        print("FAISS index successfully created and saved.")
    except Exception as e:
        logging.error(f"Error in get_vector_store: {e}")
        raise e

def user_input(user_question):
    """Fetch a response to the user's question."""
    try:
        # Log the user question
        logging.info(f"User question: {user_question}")

        # Load the FAISS index and embeddings
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

        # Perform a similarity search
        docs = vector_store.similarity_search(user_question)
        logging.info(f"Retrieved documents: {len(docs)}")

        # Load the conversational chain
        chain = get_conversational_chain()

        # Generate the response
        response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)

        # Log the AI response
        logging.info(f"AI response: {response['output_text']}")
        return response["output_text"]

    except Exception as e:
        # Log any errors encountered
        logging.error(f"Error in user_input: {e}")
        return f"An error occurred: {e}"


def get_conversational_chain():
    """Create and return the conversational chain."""
    prompt_template = """
    Answer the question as detailed as possible from the provided context.
    If the answer is not in the context, say "Answer is not available in the context."

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    return load_qa_chain(model, chain_type="stuff", prompt=prompt)
