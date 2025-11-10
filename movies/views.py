from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Movie, Review
from .filters import MovieFilter
from .forms import MovieForm
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

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
def movie_subscribe(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if not movie.subscribers.filter(id=request.user.id).exists():
        movie.subscribers.add(request.user)
    return redirect('movie_detail', pk)

def movie_unsubscribe(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if movie.subscribers.filter(id=request.user.id).exists():
        movie.subscribers.remove(request.user)
    return redirect('movie_detail', pk)


class MovieCreate(PermissionRequiredMixin, CreateView):
    permission_required = (
        'movie.view_movie',
        'movie.add_movie',
    )
    raise_exception = True
    model = Movie
    form_class = MovieForm
    template_name = 'movie_create.html'

class MovieUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = (
        'movie.view_movie',
        'movie.change_movie',
    )
    raise_exception = True
    model = Movie
    form_class = MovieForm
    template_name = 'movie_create.html'

class MovieDelete(PermissionRequiredMixin, DeleteView):
    permission_required = (
        'movie.view_movie',
        'movie.delete_movie',
    )
    raise_exception = True
    model = Movie
    template_name = 'movie_delete.html'
    context_object_name = 'movie'

class ReviewList(ListView):
    model = Review
    ordering = 'time_in'
    template_name = 'reviews.html'
    context_object_name = 'reviews'