from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.db.models import Sum
from django.urls import reverse_lazy, reverse

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=20, null=False, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    movie = 'Кинофильм'
    serial = 'Сериал'
    cartoon = 'Мультфильм'

    GENRES = [
        ('MV', movie),
        ('SR', serial),
        ('CR', cartoon),
    ]

    type = models.CharField(max_length=2, choices=GENRES)
    poster = models.ImageField(upload_to = 'image_photo/', blank=True, null=True)
    name = models.CharField(max_length=120, null=False)
    rating = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
        null=True,
    )
    year = models.DateField(null=True)
    description = models.TextField(
        blank=False,
        null=False,
        validators=[MaxLengthValidator(5000, message="Рецензия не может быть длиннее 5000 символов")]
    )
    category = models.ManyToManyField(Category, through='MovieCategory')
    def update_rating(self):
        self.rating=Review.objects.filter(movie=self).aggregate(Sum('grade'))['grade__sum']/Review.objects.filter(movie=self).count()
        self.save()
        return self.rating
    def get_absolute_url(self):
        return reverse('movie_list')

class MovieCategory(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
def get_deleted_user():
    return User.objects.get(username='deleted_user')
class Review(models.Model):

    author = models.ForeignKey(
        Author,
        on_delete=models.SET_DEFAULT,
        default=get_deleted_user
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=False, null=False)
    title = models.CharField(max_length=150, null=False)
    text = models.TextField(
        null=False,
        blank=False,
        validators=[MaxLengthValidator(5000, message="Рецензия не может быть длиннее 5000 символов")]
    )
    time_in = models.DateTimeField(auto_now_add=True)
    time_edit = models.DateTimeField(auto_now=True)
    grade = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
        null=True,
    )

class Comment(models.Model):
    def get_deleted_user(self):
        return User.objects.get(username='deleted_user')

    user = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        default=get_deleted_user,
    )
    text = models.TextField(
        null=False,
        blank=False,
        validators=[MaxLengthValidator(5000, message="Рецензия не может быть длиннее 5000 символов")]
    )
    time_in = models.DateTimeField(auto_now_add=True)
    time_edit = models.DateTimeField(auto_now=True)


