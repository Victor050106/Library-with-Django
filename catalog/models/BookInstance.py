from django.db import models
from .Book import Book
from django.urls import reverse
class Book_Instance(models.Model):
    """Model representing a book Instance."""
    unique_id = models.CharField(max_length=50)
    due_back = models.DateField(null=True,blank=True)
    
    LOAN_STATUS = (
        ('m','Maintenance'),
        ('o','On load'),
        ('a','Available'),
        ('r','Reversed'),
    )
    
    status = models.CharField(max_length=1, choices=LOAN_STATUS,blank=True,default='m',help_text='Book availability')
    book = models.OneToOneField(Book,null=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.unique_id
    
    def get_absolute_url(self):
        return reverse("bookinstance_detail", args=[str(self.id)])
    
    