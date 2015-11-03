from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    name = models.CharField(max_length=100)
    note = models.TextField()
    rate = models.IntegerField()
    user = models.ForeignKey(User)
    
    def __str__(self):
        return self.name
    