from django.db import models
from django.utils import timezone

# Create your models here.


class Genere(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    released_year = models.IntegerField()
    numbers_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genere = models.ForeignKey(Genere, on_delete=models.CASCADE)
    date_created = models.DateField(default=timezone.now)
