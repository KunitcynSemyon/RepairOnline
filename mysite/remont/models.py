from django.db import models

class Visitors(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length = 50)
    massage = models.TextField()