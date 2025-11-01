from django.urls import path
from .views import MovieList, MovieDetail, ReviewList, MovieCreate

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('<int:pk>', MovieDetail.as_view(), name='movie_detail'),
    path('reviews', ReviewList.as_view(), name='review_list'),
    path('create_movie', MovieCreate.as_view(), name='movie_create'),
]