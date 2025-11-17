from django.urls import path
from .views import (MovieList, MovieDetail, ReviewList, MovieCreate, MovieUpdate, MovieDelete, movie_subscribe,
                    movie_unsubscribe, ReviewCreate)


urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('<int:pk>', MovieDetail.as_view(), name='movie_detail'),
    path('reviews', ReviewList.as_view(), name='review_list'),
    path('create_movie', MovieCreate.as_view(), name='movie_create'),
    path('movie_update/<int:pk>', MovieUpdate.as_view(), name='movie_update'),
    path('movie_delete/<int:pk>', MovieDelete.as_view(), name='movie_delete'),
    path('movie_subscribe/<int:pk>', movie_subscribe, name='movie_subscribe'),
    path('movie_unsubscribe/<int:pk>', movie_unsubscribe, name='movie_unsubscribe'),
    path('create_review/<int:pk>', ReviewCreate.as_view(), name='create_review'),

]