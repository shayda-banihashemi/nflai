import pprint

print = pprint.pprint


def articles_gather_data():
    article_docs = []
    with open("data/nfl_article.txt", encoding='utf-8', errors='ignore') as f:
        for lines in f:
            line = lines.rstrip()
            article_docs.append(line)
    return article_docs


if __name__ == "__main__":
    articles = articles_gather_data()
    print(articles)
