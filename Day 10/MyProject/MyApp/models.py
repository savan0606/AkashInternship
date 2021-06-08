from django.db import models

# Create your models here.
class Student(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    std = models.IntegerField()
    fees = models.IntegerField()

    def __str__(self) -> str:
        return self.fname

class Teacher(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    salary = models.IntegerField()

    def __str__(self) -> str:
        return self.fname