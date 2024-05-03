from django.shortcuts import render
from django.views.generic import ListView
from .models import Course


class ListOfCourses(ListView):
    model = Course
    template_name = 'main.html'
    context_object_name = 'course'

