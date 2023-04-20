from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class Task(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in progress', 'In Progress'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    due_date = models.DateField()

    def __str__(self):
        return self.title
