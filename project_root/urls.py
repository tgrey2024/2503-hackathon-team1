"""URL configuration."""

from django.contrib import admin
from django.urls import include, path
from timeline.views import timeline

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include('home.urls')),
    path('timeline/', timeline, name='timeline'),
]
