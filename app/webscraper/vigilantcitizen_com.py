from bs4 import BeautifulSoup
import requests
import os

def get_articles(page_num):
    website_name = os.path.basename(__file__).replace("_", ".")[:-3]
    archive_url = 'https://' + website_name + '/page/' + str(page_num) + '/?s'
    resp = requests.get(archive_url)
    soup = BeautifulSoup(resp.text, 'lxml')
    article_url_tags = soup.find_all("li", {"class": "mvp-blog-story-wrap"})

    articles = []
    for article_url_tag in article_url_tags:
        article_url = article_url_tag.find("a").attrs["href"]
        resp = requests.get(article_url)
        soup = BeautifulSoup(resp.text, 'lxml')
        title_tag = soup.find("h1", {"class": "mvp-post-title"})
        if not soup.find("span", {"class": "mvp-post-excerpt"}):
            subtitle_text = ""
        else:
            subtitle_text = soup.find("span", {"class": "mvp-post-excerpt"}).find("p").text
        paragraphs = soup.find("div", {"id": "mvp-content-main"}).findAll("p")
        article_text = ""
        for paragraph in paragraphs:
            article_text += "".join('<p>' + paragraph.decode_contents() + '</p>')
        date = soup.find("time", {"class": "post-date"}).attrs["datetime"]

        articles.append({
                        "title": title_tag.text,
                        "subtitle": subtitle_text,
                        "text": article_text,
                        "url": article_url,
                        "publisher": website_name,
                        "date": date
                        })
    return articles

def grouping():
    return "by_page"

if __name__ == "__main__":
    print("module test")