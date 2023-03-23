import requests
import json
from datetime import datetime
import schedule
import time

class BaseNewsAPI:
    def __init__(self, api_key):
        self.api_key = api_key


    def backupAPI(self):
        # backup the news api for categories
        categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
        for category in categories:
            # get the news
            url = (f'https://newsapi.org/v2/top-headlines?country=mx&category={category}&apiKey={self.api_key}')
            response = requests.get(url)
            response_json = response.json()

            # save the news in a json file for each category
            with open(f'database/{category}.json', 'w') as f:
                json.dump(response_json.get('articles'), f)
        # print('Backup done...')

    def getArticles(self, category):
        # read the json file for the category
        with open(f'database/{category}.json', 'r') as f:
            articles = json.load(f)
        return articles

    def getTitle(self, article):
        return article.get('title') if article.get('title') != None else ''

    def getDescription(self, article):
        return article.get('description') if article.get('description') != None else ''

    def getUrl(self, article):
        return article.get('url') if article.get('url') != None else ''

    def getImage(self, article):
        return article.get('urlToImage') if article.get('urlToImage') != None else ''

    def getAuthor(self, article):
        return article.get('author') if article.get('author') != None else ''

    def getPublished(self, article):
        return datetime.fromisoformat(article.get('publishedAt')[:-1]) if article.get('publishedAt') != None else ''
