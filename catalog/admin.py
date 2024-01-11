from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, Collection


from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

admin.site.unregister(User)
admin.site.unregister(Group)


class CollectionCreatorMixin:
    def create_collection(self, request, queryset):
        title = f"Collection of {', '.join([obj.title for obj in queryset])}"
        collection = Collection(
            title=title,
        )
        collection.save()
        collection.book.set(queryset)

        return HttpResponseRedirect(
            reverse('admin:catalog_collection_change', args=[collection.id])
        )

    create_collection.short_description = "Create a collection from selected"


class BookAdmin(admin.ModelAdmin, CollectionCreatorMixin):
    actions = ['create_collection']

    view_on_site = False

    list_display = ('title', 'author_name', 'summary', 'score', 'genres',)
    search_fields = ['title', 'author__last_name', 'genre__genre_name']
    list_filter = ['genre__genre_name']

    def author_name(self, obj):
        return obj.author.name()

    def genres(self, obj):
        return ", ".join(obj.genres())


class AuthorAdmin(admin.ModelAdmin):
    view_on_site = False

    list_display = ('author_name', 'date_of_birth', 'date_of_death',)
    search_fields = ['last_name', 'first_name']

    def author_name(self, obj):
        return obj.name()


class GenreAdmin(admin.ModelAdmin):
    view_on_site = False

    list_display = ("genre_name",)


class CollectionAdmin(admin.ModelAdmin):
    view_on_site = False

    list_display = ('title', 'books',)
    search_fields = ['title', 'book__title']

    def books(self, obj):
        return ", ".join(obj.books())


admin.site.site_header = "Local Library"
admin.site.index_title = ""
admin.site.site_url = ''  # Removes the 'View Site' link

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Collection, CollectionAdmin)
