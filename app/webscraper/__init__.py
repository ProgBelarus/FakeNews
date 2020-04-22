from app.catalog.models import Publication, Article
import datetime
import importlib
import os

def add_articles_batch(articles, max_number_to_add=10000):
    count_added = 0
    for article in articles:
        if max_number_to_add == count_added:
            break
        if not Article.query.filter_by(title=article["title"], subtitle=article["subtitle"],
                                       text=article["text"]).first():
            if Article.create_article(title=article["title"],
                                      subtitle=article["subtitle"],
                                      text=article["text"],
                                      url=article["url"],
                                      pub_date=article["date"],
                                      pub_id=Publication.query.filter_by(name=article["publisher"]).first().id,
                                      is_gold=False
                                      ):
                count_added += 1
    return count_added

def add_articles(num_articles, pub_name):
    if not Publication.query.filter_by(name=pub_name).first():
        Publication.create_publication(name=pub_name)

    pub_module = importlib.import_module("app.webscraper." + pub_name.replace(".", "_"))

    if pub_module.grouping() == "by_page":

        page_num = 1
        num_added = 0
        while num_added < num_articles:
            if page_num >= 100:
                break
            num_added += add_articles_batch(pub_module.get_articles(page_num), num_articles - num_added)
            page_num += 1

    if pub_module.grouping() == "by_date":

        date = datetime.date.today()
        num_added = 0
        date_count = 0
        while num_added < num_articles:
            if date_count >= 50:
                break
            num_added += add_articles_batch(pub_module.get_articles(date), num_articles - num_added)
            date = date - datetime.timedelta(days=1)
            date_count += 1

def load_new_articles_to_database(num_load):
    package_filenames = os.listdir(os.path.dirname(os.path.realpath(__file__)))
    for pub_name in package_filenames:
        if pub_name == "__init__.py" or pub_name == "__pycache__":
            continue
        pub_name = pub_name[:-3].replace("_", ".")  # get website name from file name
        add_articles(num_load, pub_name)
        print(pub_name + " articles loaded")