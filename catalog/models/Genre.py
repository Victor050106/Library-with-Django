
from django.db import models
from django.urls import reverse

class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("genre_detail", args=[str(self.id)])
    