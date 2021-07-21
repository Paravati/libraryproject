from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField


class Genre(models.Model):
    type = models.CharField(max_length=25)

    def __str__(self):
        return self.type

    class Meta:
        ordering = ['type']


class Author(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="photos", default="foto.png")
    country = CountryField(blank_label='select country')

    def __str__(self):
        return self.name + " " + self.surname + " from: " + self.country.name

    def get_absolute_url(self):
        return reverse("author detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['surname']


class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    cover = models.ImageField(upload_to='book_cover', default='download.png')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['title']

