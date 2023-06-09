from django.contrib import admin

# Register your models here.

from .models.Book import Book
from .models.Author import Author
from .models.BookInstance import Book_Instance
from .models.Genre import Genre
from .models.Language import Language


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Book_Instance)
admin.site.register(Genre)
admin.site.register(Language)