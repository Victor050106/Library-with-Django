from django.views import generic

from ..models.Book import Book

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'catalog/book/book_list.html'
    
class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book_detail'
    template_name = 'catalog/book/book_detail.html'
    
class BookCreateView(generic.CreateView):
    model = Book
    fields = [
        'title',
        'author',
        'summary',
        'ISBN',
        'genre',
        'language'
    ]
    template_name = 'catalog/book/book_form.html'