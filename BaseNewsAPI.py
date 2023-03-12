import requests
import json
from datetime import datetime


class BaseNewsAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def getArticles(self, category):
        url = "https://newsapi.org/v2/top-headlines?country=mx&category={}&apiKey={}".format(category, self.api_key)
        response = requests.get(url)
        response_json = json.loads(response.text)
        return response_json.get('articles')

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
