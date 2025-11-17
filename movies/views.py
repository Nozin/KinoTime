from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Movie, Review, Author
from .filters import MovieFilter
from .forms import MovieForm, ReviewForm
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

        # Получаем все отзывы к фильму
        reviews = Review.objects.filter(movie=self.object)

        # Для каждого отзыва добавляем его комментарии
        reviews_with_comments = []
        for review in reviews:
            review_comments = review.comment_set.all()  # если внешний ключ из Comment -> Review называется comment_set
            reviews_with_comments.append({
                'review': review,
                'comments': review_comments
            })
        context['reviews_with_comments'] = reviews_with_comments
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
        'movies.view_movie',
        'movies.add_movie',
    )
    raise_exception = True
    model = Movie
    form_class = MovieForm
    template_name = 'movie_create.html'

class MovieUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = (
        'movies.view_movie',
        'movies.change_movie',
    )
    raise_exception = True
    model = Movie
    form_class = MovieForm
    template_name = 'movie_create.html'

class MovieDelete(PermissionRequiredMixin, DeleteView):
    permission_required = (
        'movies.view_movie',
        'movies.delete_movie',
    )
    raise_exception = True
    model = Movie
    template_name = 'movie_delete.html'
    context_object_name = 'movie'
    def get_success_url(self):
        return reverse_lazy('movie_list')

class ReviewList(ListView):
    model = Review
    ordering = 'time_in'
    template_name = 'reviews.html'
    context_object_name = 'reviews'

class ReviewCreate(PermissionRequiredMixin, CreateView):
    permission_required = (
        'movies.view_review',
        'movies.add_review',
    )
    raise_exception = True
    model = Review
    form_class = ReviewForm
    template_name = 'review_create.html'
    def form_valid(self, form):
        review = form.save(commit=False)
        review.author = Author.objects.get(user=self.request.user)
        review.movie = Movie.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('movie_detail', kwargs={'pk': self.kwargs['pk']})