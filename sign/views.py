from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from movies.models import Review, Author
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


class PersonalPage(LoginRequiredMixin, TemplateView):
    template_name = "personal_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context['in_author_group'] = self.request.user.groups.filter(name='author').exists()
        context['is_author_in_model'] = Author.objects.filter(user=self.request.user).exists()
        if context['is_author_in_model'] and context['in_author_group']:
            context["reviews"] = Review.objects.filter(author=Author.objects.get(user=self.request.user))
        return context
@login_required
def become_author(request):
    user = request.user
    premium_group = Group.objects.get(name='author')
    if not request.user.groups.filter(name='author').exists():
        premium_group.user_set.add(user)
    if not Author.objects.filter(user=request.user).exists():
        Author.objects.create(user=request.user)
    return redirect('movie_list')
