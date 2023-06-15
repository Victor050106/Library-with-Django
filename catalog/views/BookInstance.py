from django.views import generic

from ..models.BookInstance import Book_Instance


class BookInstanceListView(generic.ListView):
    model = Book_Instance
    context_object_name = 'book_instance_list'
    template_name = "catalog/BookInstance/book_instance_list.html"


class BookInstanceDetailView(generic.DetailView):
    model = Book_Instance
    context_object_name = 'book_instance_detail'
    template_name = "catalog/BookInstance/book_instance_detail.html"
    

class BookInstanceCreateView(generic.CreateView):
    model = Book_Instance
    fields = [
        'unique_Id',
        'due_back',
        'status',
        'book'
    ]

    template_name = 'catalog/BookInstance/book_instace_form.html'