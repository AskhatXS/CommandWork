from django.contrib import admin
from .models import Course, Assignment, Grade, Lecture

admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(Assignment)
admin.site.register(Grade)

