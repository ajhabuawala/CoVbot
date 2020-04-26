import requests
import random
import config


api_key = config.api_key

def get_movie_details():
    """docstring for get_random_movie_details"""
    all_movies = get_movies_from_db()
    random_movie = randomly_choose_a_movie(all_movies)
    movie_title, movie_plot, movie_duration = get_random_movie_details(random_movie)
    return movie_title, movie_plot, movie_duration


def get_movies_from_db():
    """docstring for get_movies_from_db"""
    global api_key
    response = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=' + api_key + '&primary_release_year=2019&sort_by=revenue.desc')
    json_data = response.json()
    all_movies = json_data['results']
    return all_movies


def randomly_choose_a_movie(all_movies):
    """docstring for randomly_choose_a_movie"""
    movies_list = [movie['id'] for movie in all_movies]
    random_movie = random.choice(movies_list)
    return random_movie


def get_random_movie_details(random_movie):
    """docstring for get_random_movie_details"""
    global api_key
    response = requests.get('https://api.themoviedb.org/3/movie/' + str(random_movie) + '?api_key=' + api_key + '&language=en-US')
    movie_detail = response.json()
    movie_title = movie_detail['title']
    movie_plot = movie_detail['overview']
    movie_duration = movie_detail['runtime']
    return movie_title, movie_plot, movie_duration


if __name__ == '__main__':
    get_movie_details()
