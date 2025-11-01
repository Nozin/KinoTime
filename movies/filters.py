from django_filters import FilterSet
from .models import Movie

class MovieFilter(FilterSet):
    class Meta:
        model = Movie
        fields ={
            'name': ['iregex'],
            'rating': ['gt'],
        }