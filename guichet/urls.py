from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('suivre', views.suivre, name='suivre')
]
