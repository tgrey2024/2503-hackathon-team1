"""URL configuration."""

from django.contrib import admin
from django.urls import include, path
from timeline.views import timeline
from home.views import index

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include('home.urls')),
    path('timeline/', timeline, name='timeline'),
    path('mentors/', include('mentors.urls')),
]
