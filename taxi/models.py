from django.db import models
from django.contrib.auth.models import AbstractUser

class Manufacturer(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    country = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.name} {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length = 100, unique = True)

class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE,
                                    related_name="cars")
    drivers = models.ManyToManyField("Driver")

    def __str__(self):
        return f"{self.model}"

