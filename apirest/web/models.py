from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class RatingBooks(models.Model):
    isbn=models.CharField(max_length=13)
    userid = models.CharField(max_length=50)
    rating=models.SmallIntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(1)])
    comment=models.CharField(max_length=250)