from django.db import models

TYPE_CHOICES = [
    ('Tugas Harian', 'Tugas Harian'),
    ('Tugas Akhir', 'Tugas Akhir'),
    ('Ujian', 'Ujian'),
]

class Assignment(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    subject = models.CharField(max_length=100)
    date = models.DateTimeField()
    progress = models.IntegerField()
    description = models.TextField()
