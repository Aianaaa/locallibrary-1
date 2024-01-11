from django.core.management.base import BaseCommand

import datetime

from catalog.models import Author, Genre, Book


class Command(BaseCommand):
    help = "Clear data in library"

    def handle(self, *args, **kwargs):
        Book.objects.all().delete()
        Genre.objects.all().delete()
        Author.objects.all().delete()
