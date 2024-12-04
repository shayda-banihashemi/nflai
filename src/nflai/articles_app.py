import pprint

print = pprint.pprint

def articles_gather_data():
    article_docs = []
    with open("/Users/shaydabanihashemi/ws/nflai/data/nfl_article.txt") as f:
        for lines in f:
            line = lines.rstrip()
            article_docs.append(line)
    return article_docs

if __name__ == "__main__":
    articles_gather_data()