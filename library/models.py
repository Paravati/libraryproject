from django.db import models
from django_countries.fields import CountryField


class Genre(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type

    class Meta:
        ordering = ['name']


class Author(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="photos", default="foto.png")
    country = CountryField(blank_label=('select country'))

    def __str__(self):
        return (self.name + " " + self.surname + " from: " + self.country)

    def get_absolute_url(self):
        return reversed()



