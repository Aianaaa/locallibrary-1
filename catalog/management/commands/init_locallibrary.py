from django.core.management.base import BaseCommand

import datetime

from catalog.models import Author, Genre, Book

GENRES = [
    Genre(genre_name='Science Fiction'),
    Genre(genre_name='Fantasy'),
    Genre(genre_name='Action & Adventure'),
    Genre(genre_name='Horror'),
    Genre(genre_name='History'),
    Genre(genre_name='Romance'),
]

AUTHORS = [
    Author(
        first_name="John R.R.",
        last_name="Tolkien",
        date_of_birth=datetime.datetime(year=1892, month=1, day=3),
        date_of_death=datetime.datetime(year=1973, month=9, day=2),
    ),
    Author(
        first_name="Isaak",
        last_name="Asimov",
        date_of_birth=datetime.datetime(year=1919, month=10, day=4),
        date_of_death=datetime.datetime(year=1992, month=4, day=6),
    ),
    Author(
        first_name="Michael",
        last_name="Crayton",
        date_of_birth=datetime.datetime(year=1942, month=10, day=23),
        date_of_death=datetime.datetime(year=2008, month=11, day=8),
    ),
    Author(
        first_name="Stephen",
        last_name="King",
        date_of_birth=datetime.datetime(year=1947, month=9, day=21),
        date_of_death=None,
    ),
    Author(
        first_name="Jared",
        last_name="Diamond",
        date_of_birth=datetime.datetime(year=1937, month=9, day=10),
        date_of_death=None,
    ),
    Author(
        first_name="Fyodor",
        last_name="Dostoevsky",
        date_of_birth=datetime.datetime(year=1821, month=11, day=11),
        date_of_death=datetime.datetime(year=1881, month=2, day=9),
    ),
]

BOOKS = [
    dict(
        title='The Lord of the Rings: The Fellowship of the Ring',
        author=AUTHORS[0],
        score=4.3,
        genre=[GENRES[1], GENRES[4]],
    ),
    dict(
        title='The Lord of the Rings: The Two Towers',
        author=AUTHORS[0],
        summary='',
        score=4.7,
        genre=[GENRES[1], GENRES[4]],
    ),
    dict(
        title='The Lord of the Rings: The Return of the King',
        author=AUTHORS[0],
        summary='',
        score=4.9,
        genre=[GENRES[1], GENRES[4]],
    ),

    dict(
        title='The End of Eternity',
        author=AUTHORS[1],
        summary='',
        score=4.1,
        genre=[GENRES[0]],
    ),

    dict(
        title='The Jurassic Park',
        author=AUTHORS[2],
        summary='',
        score=4.3,
        genre=[GENRES[0], GENRES[2]],
    ),

    dict(
        title='It',
        author=AUTHORS[3],
        summary='',
        score=4.3,
        genre=[GENRES[3]],
    ),

    dict(
        title='Guns, Germs, and Steel: The Fates of Human Societies',
        author=AUTHORS[4],
        summary='',
        score=3.5,
        genre=[GENRES[4]],
    ),

    dict(
        title='The Brothers Karamazov',
        author=AUTHORS[5],
        summary='',
        score=4.0,
        genre=[GENRES[5]],
    ),
]


class Command(BaseCommand):
    help = "Create initial data in database"

    def handle(self, *args, **kwargs):
        for author in AUTHORS:
            author.save()
        for genre in GENRES:
            genre.save()
        for book in BOOKS:
            m_book = Book(
                title=book['title'],
                author=book['author'],
                score=book['score'],
            )
            m_book.save()
            m_book.genre.set(book['genre'])
