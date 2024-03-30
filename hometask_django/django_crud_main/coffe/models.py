from django.db import models
from django.contrib.auth.models import User


class Coffee(models.Model):
    drink_type = models.CharField(max_length=50)
    price_small = models.DecimalField(max_digits=5, decimal_places=2)
    price_medium = models.DecimalField(max_digits=5, decimal_places=2)
    price_large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.drink_type}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    text = models.TextField()
