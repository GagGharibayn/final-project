import requests
import sqlite3

class OMDBAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://www.omdbapi.com/"

    def get_movie_details(self, movie_title):
        params = {
            "apikey": self.api_key,
            "t": movie_title
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            movie_data = response.json()
            return movie_data
        else:
            print(f"Failed to retrieve data: {response.content}")
            return None

    def display_info(self):
        movie_title = input('Please enter movie name: ')
        movie_details = self.get_movie_details(movie_title)
        if movie_details:
            print(f"Title: {movie_details['Title']}")
            print(f"Year: {movie_details['Year']}")
            print(f"Genre: {movie_details['Genre']}")
            print(f"Actors: {movie_details['Actors']}")
            print(f"Language: {movie_details['Language']}")
            print(f"Box Office: {movie_details['BoxOffice']}")
            print(f"Rating: {movie_details['imdbRating']}")
        else:
            print("Failed to retrieve movie details.")

    def check_have_movie_db(self, movie_title):
        with sqlite3.connect('movies_project.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Movies WHERE movie_name = ?", (movie_title,))
            movie = cursor.fetchone()
        return movie is not None

    def add_movie(self, movie_details):
        with sqlite3.connect('movies_project.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO Movies(movie_name, year, genre, language, imbd_rating, box_office)
             VALUES(?, ?, ?, ?, ?, ?)''',
                           (movie_details['Title'], movie_details['Year'], movie_details['Genre'],
                            movie_details['Language'], movie_details['imdbRating'], movie_details['BoxOffice']))
