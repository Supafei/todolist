from django.db import models

# Create your models here.

class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    status = models.BooleanField(default=False)

class Meta:
    ordering = ['created']