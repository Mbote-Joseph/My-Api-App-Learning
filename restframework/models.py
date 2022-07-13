from re import M
from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.
class Book(models.Model):
    name= models.CharField(max_length=255)
    price= models.FloatField()
    stock= models.IntegerField()
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name