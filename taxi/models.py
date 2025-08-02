from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth.models import AbstractUser

class Manufacture(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    country = models.CharField(max_length = 100)

class Car(models.Model):
    model = models.CharField(max_length = 100)
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE,
                                    related_name = "cars")
    drivers = models.ManyToManyField(Driver)

class Driver(AbstractUser):
    license_number = models.CharField(max_length = 100, unique = True)

