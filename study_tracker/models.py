from django.db import models

class Assignment(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    date = models.DateTimeField()
    progress = models.IntegerField()
    description = models.TextField()
