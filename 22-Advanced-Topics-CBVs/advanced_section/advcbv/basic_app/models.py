from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=264)
    principal = models.CharField(max_length=264)
    location = models.CharField(max_length=264)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:details", kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length=264)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name