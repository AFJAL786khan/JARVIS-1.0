import requests
from bs4 import BeautifulSoup
from Body.Speak import Speak
import pyttsx3

def news_fetcher():
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        url_news = requests.get('https://www.hindustantimes.com/', headers=headers).text

        soup = BeautifulSoup(url_news, "lxml")

        news = soup.find_all('div', class_ = 'cartHolder listView track timeAgo')

        count = 0
        for index, news_list in enumerate(news):
            article = news_list.find('h3', class_ = 'hdg3').text
            print(f'{index + 1} {article}')
            Speak(article)
            count += 1

            if count == 10:
                break
    except Exception:
        Speak("There has been some error")
        print("There has been some error")