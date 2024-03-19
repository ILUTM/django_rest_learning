from django.db import models

class Car(models.Model):
    model = models.CharField(max_length=60)
    color = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return f'{self.model} | {self.color} | {self.year}'
