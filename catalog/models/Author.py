from django.db import models


class Author(models.Model):
    """Model representing a book author."""
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(default=0)
    date_of_death = models.DateField(default=0)

    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("author_detail", args=[str(self.id)])
    