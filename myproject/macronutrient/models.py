from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    name = models.CharField(max_length=90)
    glucids = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()

    def __str__(self):
        return self.name
    
class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)