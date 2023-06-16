from django.shortcuts import render

# Create your views here.
from ..models.Author import Author
from ..models.Book import Book
from ..models.BookInstance import Book_Instance
from ..models.Genre import Genre
from ..models.Language import Language

def index(request):
    """function to home site"""
    author = Author.objects.all()
    book = Book.objects.all()
    book_Instance = Book_Instance.objects.all()
    genres = Genre.objects.all()
    languages = Language.objects.all()
    
    return render(
        request,
        'catalog/index.html',
        context=
        {
            "author":author,
            "book":book,
            "book_Instance": book_Instance,
            "genre":genres,
            "language":languages
        }
    )