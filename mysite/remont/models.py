from django.db import models

class Visitors(models.Model):
    name = models.CharField(max_length = 20)
    sender = models.CharField(max_length = 20)
    message = models.CharField(max_length = 128)
    