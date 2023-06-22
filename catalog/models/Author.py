from django.db import models
from django.urls import reverse



class Author(models.Model):
    """Model representing a book author."""
    fname = models.CharField(max_length=50, help_text="Enter first name of Author")
    lname = models.CharField(max_length=50, help_text="Enter last name of Author")
    date_of_birth = models.DateField(null=False,blank=False,help_text="Enter date of birth of Author")
    date_of_death = models.DateField('Died',null=True,blank=True,help_text="Enter date of death of Author")

    
    def __str__(self):
        return self.fname + self.lname
    
    def get_absolute_url(self):
        return reverse("author_detail", args=[str(self.id)])
    