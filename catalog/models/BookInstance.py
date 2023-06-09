from django.db import models
from .Book import Book

class Book_Instance(models.Model):
    unique_Id = models.CharField(max_length=50)
    due_back = models.DateField(default=0)
    status = models.CharField(max_length=50)
    book = models.OneToOneField(Book,null=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.unique_Id
    