from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie, Review

class MovieList(ListView):
    model = Movie
    ordering = 'year'
    template_name = 'movies.html'
    context_object_name = 'movies'
    paginate_by = 1

class MovieDetail(DetailView):
    model = Movie
    template_name = 'movie.html'
    context_object_name = 'movie'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(movie=self.object)#self.review_set.all() #Review.objects.order_by('-dataCreation').filter(commentPost_id=self.id)
        return context

class ReviewList(ListView):
    model = Review
    ordering = 'time_in'
    template_name = 'reviews.html'
    context_object_name = 'reviews'