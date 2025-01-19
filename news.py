from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_news():
    api_key = '25ccf200a52747c89e874e470d1a3a89'
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(url)
    return response.json().get('articles', [])




