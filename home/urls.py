from django.urls import path
from . import views
from .views import index, about

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', about, name='about'),
]
