from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    maths = models.IntegerField()
    science = models.IntegerField()
    history = models.IntegerField()

