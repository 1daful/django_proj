from django.urls import path
from . import views

urlpatterns = [
    path('recognise/', views.recognise_face, name='recognise_face'),
]