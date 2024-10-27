import chromadb
from peewee import sqlite3

import nflai.weeks_app
import nflai.seasons_app
import nflai.articles_app
import duckdb
from chromadb.config import Settings
from chromadb.utils import embedding_functions

RELOAD_DB = True

chroma_client = chromadb.PersistentClient(
    path="./database",
    settings=Settings(anonymized_telemetry=False))

collection = chroma_client.get_or_create_collection(name="my_collection")

def agg_data():

    seasons = nflai.seasons_app.seasons_gather_data()
    weeks = nflai.weeks_app.weeks_gather_data()
    articles = nflai.articles_app.articles_gather_data()
    all_docs = articles + weeks + seasons
    return all_docs

def load_data(docs):

    ids = [f"id{num}" for num in range(1, len(docs) +1 )]
    collection.upsert(documents=docs, ids=ids)

def query():
    run_query = collection.query(
        query_texts=["what information is there on Baltimore"],
        n_results=2)
    return run_query

if RELOAD_DB:
    results = agg_data()
    load_data(results)
    findings = query()

print(findings)







