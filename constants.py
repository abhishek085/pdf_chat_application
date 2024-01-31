#this file is for chroma db settings
import os
from chromadb.config import Settings

#define the chroma settings
# chroma_db_impl - implementation (store the embedings in parquet format through duckdb )
#persist directory = db folder path
#anonymized telementry is false


CHROMA_SETTINGS = Settings(
    chroma_db_impl = 'duckdb+parquet',
    persist_directory = 'db',
    anonymized_telemetry = False
)