from django.views import generic

from ..models.Language import Language

class LanguageListView(generic.ListView):
    model = Language
    context_object_name = 'language_list'
    template_name = "catalog/language/.html"
    
class LanguageDetailView(generic.DetailView):
    model = Language
    context_object_name = 'language_detail'
    template_name = "catalog/language/language_detail.html"

class LanguageCreateView(generic.CreateView):
    model = Language
    fields = [
        'name'
    ]
    template_name = 'catalog/language/language_form.html'
    
