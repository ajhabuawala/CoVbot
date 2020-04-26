import requests
import random
import config

api_key = config.api_key


def get_tv_show_details():
    """docstring for get_tv_show_details"""
    all_shows = get_tv_show_from_db()
    random_show = randomly_choose_a_show(all_shows)
    show_name, show_plot, show_rating = get_random_tv_show_details(random_show)
    print(show_name, show_plot, show_rating)
    return show_name, show_plot, show_rating


def get_tv_show_from_db():
    """docstring for get_tv_show_from_db"""
    global api_key
    response = requests.get('https://api.themoviedb.org/3/tv/popular' + '?api_key=' + api_key + '&language=en-US')
    json_data = response.json()
    all_tv_shows = json_data['results']
    return all_tv_shows


def randomly_choose_a_show(all_tv_shows):
    """docstring for randomly_choose_a_tv_show"""
    show_list = [tv_show['id'] for tv_show in all_tv_shows]
    random_show = random.choice(show_list)
    return random_show


def get_random_tv_show_details(random_show):
    """docstring for get_random_movie_details"""
    global api_key
    response = requests.get('https://api.themoviedb.org/3/tv/' + str(random_show) + '?api_key=' + api_key + '&language=en-US')
    show_detail = response.json()
    show_title = show_detail['name']
    show_plot = show_detail['overview']
    show_rating = show_detail['vote_average']
    return show_title, show_plot, show_rating


if __name__ == '__main__':
    get_tv_show_details()
