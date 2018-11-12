from django.db import models

class Alarm(models.Model):
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10)
    comment = models.TextField(max_length=500)
    link_video = models.TextField(max_length=500)