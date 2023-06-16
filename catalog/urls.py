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
    path("author",Author.AuthorListview.as_view(), name="Author"),
    path("author/<int:pk>",Author.AuthorDetailView.as_view(),name="Author_detail"),
    path("author/create",Author.AuthorCreateView.as_view(),name="create_author")
]

urlpatterns += [
    path("book",Book.BookListView.as_view(),name='Book'),
    path("book/<int:pk>",Book.BookDetailView.as_view(),name='book_detail'),
    path("book/create",Book.BookCreateView.as_view(),name= 'create_Book')
]

urlpatterns += [
    path("bookinstance",BookInstance.BookInstanceListView.as_view(),name='BookInstance'),
    path("bookinstance/<int:pk>",BookInstance.BookInstanceDetailView.as_view(),name='book_instance_detail'),
    path("bookinstance/create",BookInstance.BookInstanceCreateView.as_view(),name= 'create_book_instance')
]

urlpatterns += [
    path("genre",Genre.GenreListView.as_view(),name='Genre'),
    path("genre/<int:pk>",Genre.GenreDetailView.as_view(),name='Genre_detail'),
    path("genre/create",Genre.GenreCreateView.as_view(),name= 'create_Genre')
]

urlpatterns += [
    path("language",Language.LanguageListView.as_view(),name='Language'),
    path("language/<int:pk>",Language.LanguageDetailView.as_view(),name='Language_detail'),
    path("language/create",Language.LanguageCreateView.as_view(),name= 'Language_Genre')
]