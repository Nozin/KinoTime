from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Movie, Review
from .filters import MovieFilter
from .forms import MovieForm
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse

class MovieList(ListView):
    model = Movie
    ordering = 'year'
    template_name = 'movies.html'
    context_object_name = 'movies'
    paginate_by = 20

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        self.filterset = MovieFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class MovieDetail(DetailView):
    model = Movie
    template_name = 'movie.html'
    context_object_name = 'movie'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(movie=self.object)#self.review_set.all() #Review.objects.order_by('-dataCreation').filter(commentPost_id=self.id)
        return context

class MovieCreate(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movie_create.html'

class MovieUpdate(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movie_create.html'

class ReviewList(ListView):
    model = Review
    ordering = 'time_in'
    template_name = 'reviews.html'
    context_object_name = 'reviews'