import chromadb
import nflai.seasons
from chromadb.utils import embedding_functions
chroma_client = chromadb.PersistentClient(path="./database")

data_list = []
with open("/Users/shaydabanihashemi/ws/nflai/data/general/nfl_article.txt") as f:
    for lines in f:
        line = lines.rstrip()  # remove the newline character
        data_list.append(line)  # add the line in the list
    print(data_list)
collection = chroma_client.get_or_create_collection(name="my_collection") #will add embedding function later
collection.upsert(documents=data_list,

ids=["id1", "id2", "id3", "id4", "id5", "id6", "id7", "id8", "id9", "id10",
         "id11", "id12", "id13", "id14", "id15","id16", "id17", "id18", "id19",
         "id20", "id21", "id22", "id23", "id24", "id25", "id26", "id27", "id28",
         "id29", "id30", "id31", "id32"])

results = collection.query(
    query_texts=["which team has the highest probability of losing next year"],
    n_results=2
)

print(results)

data = nflai.seasons.gather_data()
print(data)




