
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import DocArrayInMemorySearch
from IPython.display import display, Markdown

from langchain.document_loaders.pdf import UnstructuredPDFLoader

def create_qa_agent(file_path):

    loader = UnstructuredPDFLoader(file_path=file_path)

    from langchain.indexes import VectorstoreIndexCreator

    index = VectorstoreIndexCreator(
        vectorstore_cls=DocArrayInMemorySearch
    ).from_loaders([loader])

    return index
