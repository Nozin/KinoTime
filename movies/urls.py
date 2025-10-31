from django.urls import path
from .views import MovieList, MovieDetail, ReviewList

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('<int:pk>', MovieDetail.as_view(), name='movie_detail'),
    path('reviews', ReviewList.as_view(), name='review_list'),
]