import pathlib

cwd = pathlib.Path.cwd()
file_dir =  cwd
myfile = file_dir / 'data' / 'nfl_article.txt'

def articles_gather_data():
    article_docs = []
    with open(myfile) as f:
        for lines in f:
            line = lines.rstrip()
            article_docs.append(line)
    return article_docs

if __name__ == "__main__":
    articles_gather_data()