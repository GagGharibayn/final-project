import random
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class RandomMovie:
    GENRES = ['War cinema', 'Detective', 'Mystic', 'Melodrama',
              'Action', 'Horror', 'Fantastic', 'Comedy']

    def recommender_movie_genre(self):
        return random.choice(self.GENRES)

    def selenium_search_movie(self, genre):
        driver = webdriver.Chrome()
        driver.get('https://www.google.com')
        search_input = driver.find_element(By.NAME, 'q')
        search_query = f'{genre} Movie'
        search_input.send_keys(search_query)
        search_input.send_keys(Keys.RETURN)
        redirected_url = driver.current_url
        driver.quit()
        return redirected_url

    def scrapping_page(self, url):
        html_request = requests.get(url).text
        soup = BeautifulSoup(html_request, 'lxml')
        movie_name = soup.find('div', class_='NJU16b')
        return movie_name
