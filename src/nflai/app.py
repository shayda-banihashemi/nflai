import chromadb
import nflai.weeks_app
import nflai.seasons_app
import nflai.articles_app
from chromadb.utils import embedding_functions
chroma_client = chromadb.PersistentClient(path="./database")

seasons = nflai.seasons_app.seasons_gather_data()
weeks = nflai.weeks_app.weeks_gather_data()
articles = nflai.articles_app.articles_gather_data()

all_docs = articles + weeks + seasons

ids = []
for x in range(len(all_docs)):
    ids.append(f"id{x}")

collection = chroma_client.get_or_create_collection(name="my_collection")
collection.upsert(documents=all_docs,ids=ids)

results = collection.query(
    query_texts=["what information is there on Baltimore"],
    n_results=2
)

print(results)







