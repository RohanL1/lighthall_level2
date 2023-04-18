from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in progress', 'In Progress'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    due_date = models.DateField()

    def __str__(self):
        return self.title
