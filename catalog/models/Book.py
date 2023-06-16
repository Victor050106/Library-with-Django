from django.db import models
from django.urls import reverse
from .Author import Author
from .Genre import Genre
from .Language import Language

class Book(models.Model):
    """Model representing a book ."""
    title = models.CharField(max_length=200)
    author = models.OneToOneField(Author,null=True, on_delete=models.CASCADE )
    summary = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre,null=True,on_delete=models.SET_NULL)
    language = models.ForeignKey(Language,null=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])
    