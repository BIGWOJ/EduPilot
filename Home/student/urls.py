from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.students_list, name='students_list'),
    path('add/', views.add_student, name='add_student'),
]
