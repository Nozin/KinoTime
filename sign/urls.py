from django.urls import path
from .views import PersonalPage, become_author

urlpatterns = [
    path('lk/', PersonalPage.as_view(), name='personal_page'),
    path('become_author/', become_author, name = 'become_author'),
]