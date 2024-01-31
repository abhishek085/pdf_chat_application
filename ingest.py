# This file is for langchain and core DL code

from langchain.document_loaders import PyPDFLoader, DirectoryLoader, PDFMinerLoader #load pdf file
from langchain.text_splitter import RecursiveCharacterTextSplitter #split text
from langchain.embeddings import SentenceTransformerEmbeddings  #create embeddings
from langchain.vectorstores import Chroma #store in db
import os 
# from constants import CHROMA_SETTINGS

persist_directory = "db"

def main():
    for root, dirs, files in  os.walk("docs"):
        for file in files:
            if file.endswith(".pdf"):
                print(file)
                loader = PDFMinerLoader(os.path.join(root,file))
    
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 500)
    texts = text_splitter.split_documents(documents=documents)
    
    #create embeddings
    embeddings = SentenceTransformerEmbeddings(model_name = "all-MiniLM-L6-v2")
    
    #create vector store
    vectordb = Chroma.from_documents(texts,embeddings,persist_directory=persist_directory)
    
    vectordb.persist()
    vectordb = None
    
if __name__ == "__main__":
    main()    
                

