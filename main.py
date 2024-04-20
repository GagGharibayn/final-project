from database import *
from authentication import *
from recomindate_search_movie import *
from omdb_api import *


def main():
    create_db_for_account()
    create_db_for_interests()
    create_db_for_movies()

    account = Account()
    api_key = '35652b5f'
    omdb_api = OMDBAPI(api_key)

    account_choice = input('Would you like to sign in or register (signin/register):\t').lower()

    if account_choice == 'signin':
        if account.signin():
            account_choice_info = input(
                'Would you like to input your lover Actors, Serials, Films and genres (yes/no):\t').lower()
            if account_choice_info == 'yes':
                account.account_info()
    elif account_choice == 'register':
        if account.registration():
            account_choice_info = input(
                'Would you like to input your lover Actors, Serials, Films and genres (yes/no):\t').lower()
            if account_choice_info == 'yes':
                account.account_info()
    else:
        print('Invalid choice. Please choose either "signin" or "register".')

    search_movie_choice = input('Do you want to search movie (yes/no):\t').lower()
    if search_movie_choice == 'yes':
        omdb_api.display_info()
        movie_title = input('Enter the movie title you want to add to the database:\t')
        if not omdb_api.check_have_movie_db(movie_title):
            movie_details = omdb_api.get_movie_details(movie_title)
            if movie_details:
                omdb_api.add_movie(movie_details)
    else:
        recommend_movie = input('Can I help you to recommend a movie (yes/no):\t').lower()
        if recommend_movie == 'yes':
            movie_recommender = RandomMovie()
            genre = movie_recommender.recommender_movie_genre()
            redirected_url = movie_recommender.selenium_search_movie(genre)
            movie_name = movie_recommender.scrapping_page(redirected_url)
            print(f'Cinema genre is: {genre}, Cinema name is: {movie_name}')


if __name__ == '__main__':
    main()
