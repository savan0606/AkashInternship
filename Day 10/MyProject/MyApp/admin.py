from MyApp.models import Student
from django.contrib import admin
from .models import Student,Teacher

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)