import requests
from bs4 import BeautifulSoup
import random


def get_random_book():
    raw_books = _get_books_from_db()
    all_books = _extract_book_details(raw_books)
    random_book_name, random_book_overview, random_book_img = _return_random_book(all_books)
    return random_book_name, random_book_overview, random_book_img


def _get_books_from_db():
    url = 'https://thegreatestbooks.org/'
    src = requests.get(url).text
    soup = BeautifulSoup(src, 'lxml')
    raw_books = soup.find_all('li', class_='item pb-3 pt-3 border-bottom')
    return raw_books


def _extract_book_details(raw_books):
    book_name = []
    book_summary = []
    book_image = []

    for book in raw_books:
        book_name.append(book.h4.a.text)
        book_summary.append(book.p.text)
        book_image.append(book.find('div', class_='pull-left mr-3').a.find('img')['src'])

    all_books = list(zip(book_name, book_summary, book_image))
    return all_books


def _return_random_book(all_books):
    random_book_details = random.choice(all_books)
    return random_book_details[0], random_book_details[1].lstrip(), random_book_details[2]


if __name__ == '__main__':
    name, overview, img = get_random_book()
    print(name)
    print(overview)
