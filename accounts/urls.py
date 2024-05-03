from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListOfCourses.as_view(), name='course')
]