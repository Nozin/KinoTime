from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=20, null=False, unique=True)

class Movie(models.Model):
    movie = 'Кинофильм'
    serial = 'Сериал'
    cartoon = 'Мультфильм'

    GENRES = [
        ('MV', movie),
        ('SR', serial),
        ('CR', cartoon),
    ]

    genre = models.CharField(max_length=2, choices=GENRES)
    type = models.CharField()
    name = models.CharField(max_length=120, null=False)
    rating = models.FloatField(max_length=10)
    description = models.TextField(null=False) #need validator
    category = models.ManyToManyField(Category, through='MovieCategory')

class MovieCategory(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Review(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE) #need to rebuild for SET_DEFAULT
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=False)
    text = models.TextField() #need validator
    time_in = models.DateTimeField(auto_now_add=True)
    time_edit = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL) #need to rebuild for SET_DEFAULT
    text = models.TextField() #need validator
    time_in = models.DateTimeField(auto_now_add=True)
    time_edit = models.DateTimeField(auto_now=True)
