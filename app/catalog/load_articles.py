import app.catalog.webscraper.antiwar_com as antiwar_com
import app.catalog.webscraper.madworldnews_com as madworldnews_com
import app.catalog.webscraper.infostormer_com as infostormer_com
import app.catalog.webscraper.conservativedailypost_com as conservativedailypost_com
import app.catalog.webscraper.vigilantcitizen_com as vigilantcitizen_com
import app.catalog.webscraper.freedomdaily_com as freedomdaily_com
import app.catalog.webscraper.clashdaily_com as clashdaily_com
import app.catalog.webscraper.dailysurge_com as dailysurge_com
import app.catalog.webscraper.newswithviews_com as newswithviews_com

def load_new_articles_to_database(num_load):
    antiwar_com.add_articles(num_load)
    print("antiwar_com articles loaded")
    madworldnews_com.add_articles(num_load)
    print("madworldnews_com articles loaded")
    infostormer_com.add_articles(num_load)
    print("infostormer_com articles loaded")
    conservativedailypost_com.add_articles(num_load)
    print("conservativedailypost_com articles loaded")
    vigilantcitizen_com.add_articles(num_load)
    print("vigilantcitizen_com articles loaded")
    freedomdaily_com.add_articles(num_load)
    print("freedomdaily_com articles loaded")
    clashdaily_com.add_articles(num_load)
    print("clashdaily_com articles loaded")
    dailysurge_com.add_articles(num_load)
    print("dailysurge_com articles loaded")
    newswithviews_com.add_articles(num_load)
    print("newswithviews_com articles loaded")