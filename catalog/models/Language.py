
from django.db import models
from django.urls import reverse
class Language(models.Model):
    """Model representing a book language."""
    name = models.CharField(max_length=35,help_text="Enter book language ")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("language_detail", args=[str(self.id)])
    