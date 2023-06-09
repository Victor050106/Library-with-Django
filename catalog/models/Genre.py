
from django.db import models

class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name