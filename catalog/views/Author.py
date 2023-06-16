from django.views import generic

from ..models.Author import Author

class AuthorListview(generic.ListView):
    model = Author
    context_object_name = 'author_list'
    template_name = 'catalog/author/author_list.html'
    


class AuthorDetailView(generic.DetailView):
    model = Author
    context_object_name = 'author_detail'
    template_name = "catalog/author/author_detail.html"
    


class AuthorCreateView(generic.CreateView):
    model = Author
    fields = [
        'fname',
        'lname',
        'date_of_birth',
        'date_of_death'
    ]

    template_name = 'catalog/author/author_form.html'
