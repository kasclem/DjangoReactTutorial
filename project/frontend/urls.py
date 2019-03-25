from django.urls import path

from project.frontend import views

urlpatterns = [
    path('', views.index),
]