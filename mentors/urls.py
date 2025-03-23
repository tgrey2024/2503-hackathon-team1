from django.urls import path

from . import views

app_name = 'mentors'

urlpatterns = [
    path('', views.mentor_list, name='mentor_list'),
    path('contact/', views.contact_form, name='contact_form'),
    path(
        'contact/<int:mentor_id>/', views.contact_form, name='contact_mentor'
    ),
    path('contact/success/', views.contact_success, name='contact_success'),
]
