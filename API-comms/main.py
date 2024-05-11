# pip dependencies: python-dotenv
import os
from dotenv import load_dotenv, dotenv_values
from aicluster import GeminiAI

from langchain_community.document_loaders import HuggingFaceDatasetLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Initialize dataset
dataset_name = "databricks/databricks-dolly-15k"
page_content_column = "response"

# Initialize dataset Loader using HuggingFaceDatasetLoader
loader = HuggingFaceDatasetLoader(dataset_name, page_content_column)

data = loader.load()

# data[:2]

# Text Chunks using RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)

docs = text_splitter.split_documents(data)



def prep():
    load_dotenv()

def main():
    prep()
    aiobj = GeminiAI(os.getenv("GEMINI_API_KEY"))
    # aiobj.get_response_default("Who was elected the president of the US in 2012")

if __name__ == "__main__":
    main()
