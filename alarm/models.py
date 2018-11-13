from django.db import models

class Alarm(models.Model):
    time = models.TimeField()
    status = models.CharField(max_length=10, default='activate')
    comment = models.CharField(max_length=500)
    link_video = models.CharField(max_length=500)