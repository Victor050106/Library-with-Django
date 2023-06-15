from django.db import models
from .Author import Author
from .Genre import Genre
from .Language import Language

class Book(models.Model):
    """Model representing a book ."""
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Author,null=True, on_delete=models.SET_NULL )
    summary = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre,null=True,on_delete=models.SET_NULL)
    language = models.ForeignKey(Language,null=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])
    