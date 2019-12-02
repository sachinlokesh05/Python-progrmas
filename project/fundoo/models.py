from django.db import models

# Create your models here.


class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100, default=first_name)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    confirm_passowrd = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name
