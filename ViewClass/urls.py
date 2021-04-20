from django.contrib import admin
from django.urls import path, include
from ViewClass import views


urlpatterns = [

    path('course/<int:pk>/',views.home,name='home_class'),
    path('course/lecture/<int:lecture_pk>/',views.lectureviewclass,name='lectureviewclass'),
    ]