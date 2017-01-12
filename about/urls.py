from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView

urlpatterns = [
    url(r'^$', views.show_about, name = 'about')
]