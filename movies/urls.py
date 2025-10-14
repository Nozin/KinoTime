from django.urls import path
from .views import MovieList, MovieDetail

urlpatterns = [
    path('', MovieList.as_view()),
    path('<int:pk>', MovieDetail.as_view(), name='movie_detail')
]