from unicodedata import name
from django.db import models

# Create your models here.
class Menu(models.Model):
    item_name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()
    popularity = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name + " : " + self.cuisine

class Person(models.Model): 
    last_name = models.TextField() 
    first_name = models.TextField() 

    def __str__(self): 
        return f"{self.last_name}, {self.first_name}" 