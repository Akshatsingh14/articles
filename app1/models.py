from django.db import models

# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length=32)
    company = models.CharField(max_length=32)
    price = models.IntegerField()
    genre = models.CharField(max_length=32)
    quantity = models.IntegerField()
    rating = models.FloatField()  
    desc = models.CharField(max_length=1000, default = 'hello')


    def __str__(self):
        return self.name