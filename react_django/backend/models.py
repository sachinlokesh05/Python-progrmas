from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# User = get_user_model()

Rating = [
    ('b', 'Bad'),
    ('a', 'Average'),
    ('e', 'Excellent')
]

gender = [
    ('m', 'male'),
    ('f', 'female')
]


class Student(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=2, choices=gender)
    cource = models.CharField(max_length=20)
    ratings = models.CharField(max_length=50, choices=Rating)

    def __str__(self):
        return str(self.name)


class Parent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=100, blank=True)
    place = models.CharField(max_length=100)
