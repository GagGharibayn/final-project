import sqlite3


def create_db_for_account():
    with sqlite3.connect('movies_project.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Account(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nick STRING NOT NULL,
        email STRING NOT NULL UNIQUE,
        password STRING NOT NULL
        )''')


def create_db_for_interests():
    with sqlite3.connect('movies_project.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Account_info(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           loves_film_name STRING,
           loves_serial_name STRING,
           loves_genre_name1 STRING,
           loves_genre_name2 STRING,
           loves_genre_name3 STRING,
           loves_actor STRING,
           account_id INTEGER,
           FOREIGN KEY (account_id) REFERENCES Account(id)
           )''')


def create_db_for_movies():
    with sqlite3.connect('movies_project.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Movies(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               movie_name STRING,
               year INTEGER,
               genre STRING,
               language STRING,
               imbd_rating INTEGER,
               box_office INTEGER
               )''')
