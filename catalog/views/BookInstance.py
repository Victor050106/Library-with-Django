from django.views import generic

from ..models.BookInstance import Book_Instance


class BookInstanceListView(generic.ListView):
    model = Book_Instance
    context_object_name = 'bookinstance_list'
    template_name = "catalog/BookInstance/bookinstance_list.html"


class BookInstanceDetailView(generic.DetailView):
    model = Book_Instance
    context_object_name = 'bookinstance_detail'
    template_name = "catalog/BookInstance/bookinstance_detail.html"
    

class BookInstanceCreateView(generic.CreateView):
    model = Book_Instance
    fields = [
        'unique_id',
        'due_back',
        'status',
        'book'
    ]

    template_name = 'catalog/BookInstance/bookinstace_form.html'