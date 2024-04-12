from langchain_community.document_loaders import TextLoader, PyPDFLoader, OnlinePDFLoader, UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import os
from langchain_community.vectorstores import Chroma, Pinecone
from langchain_openai import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY, model="text-embedding-3-large")

file_path = "/Users/swayampatil/SymptomSage/Corpus for Chatbot/Med-Book.pdf"

loader = TextLoader(file_path=file_path, encoding='latin-1')  # Specify the encoding here
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(data)

vectorstore = Chroma.from_documents(texts, embeddings)
#
# query = "what is common cold?"
# docs = vectorstore.similarity_search(query)
# for doc in docs:
#     print(f"{doc.page_content}\n")

llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
chain = load_qa_chain(llm, chain_type="stuff")

query = "What is great about having kids?"
docs = vectorstore.similarity_search(query)
chain.run(input_documents=docs, question=query)
