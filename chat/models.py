from django.db import models
from datetime import datetime

# Create your models here.

class room(models.Model):
    name = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name


class message(models.Model):
    value = models.TextField()
    date = models.DateTimeField(default=datetime.now,blank=True)
    user = models.CharField(max_length=1000)
    room = models.CharField(max_length=10000)

    def __str__(self):
        return self.user