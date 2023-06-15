from django.urls import path

from .views import views
from .views import Author
from .views import Book
from .views import BookInstance
from .views import Genre
from .views import Language

urlpatterns = [
    path('',views.index, name="index")
]

urlpatterns += [
    path("Author",Author.AuthorListview.as_view(), name="Author"),
    path("Author/<int:pk>",Author.AuthorDetailView.as_view(),name="Author_detail"),
    path("Author/create",Author.AuthorCreateView.as_view(),name="create_author")
]

urlpatterns += [
    path("Book",Book.BookListView.as_view(),name='Book'),
    path("Book/<int:pk>",Book.BookDetailView.as_view(),name='book_detail'),
    path("Book/create",Book.BookCreateView.as_view(),name= 'create_Book')
]

urlpatterns += [
    path("BookInstance",BookInstance.BookInstanceListView.as_view(),name='BookInstance'),
    path("BookInstance/<int:pk>",BookInstance.BookInstanceDetailView.as_view(),name='book_instance_detail'),
    path("BookInstance/create",BookInstance.BookInstanceCreateView.as_view(),name= 'create-book_instance')
]

urlpatterns += [
    path("Genre",Genre.GenreListView.as_view(),name='Genre'),
    path("Book/<int:pk>",Genre.GenreDetailView.as_view(),name='Genre_detail'),
    path("Book/create",Genre.GenreCreateView.as_view(),name= 'create_Genre')
]

urlpatterns += [
    path("Language",Language.LanguageListView.as_view(),name='Language'),
    path("Book/<int:pk>",Language.LanguageDetailView.as_view(),name='Language_detail'),
    path("Book/create",Language.LanguageCreateView.as_view(),name= 'Language_Genre')
]