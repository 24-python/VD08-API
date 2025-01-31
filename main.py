from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    error_message = None  # Для хранения сообщения об ошибке
    news = None

    if request.method == 'POST':
        city = request.form.get('city')
        weather = get_weather(city)
        news = get_news()
        if weather is None:
            error_message = 'Город не найден. Попробуйте еще раз.'

    return render_template('index.html', weather=weather, error_message=error_message, news=news)


def get_weather(city):
    api_key = '9a413fcf19cd15b44a83d892376d8546'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            # Specific case for city not found
            return None
        else:
            print(f'HTTP error occurred: {http_err}')
            return None
    except Exception as err:
        print(f'Other error occurred: {err}')
        return None

def get_news():
    api_key = '25ccf200a52747c89e874e470d1a3a89'
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(url)
    return response.json().get('articles', [])

if __name__ == '__main__':
    app.run()
