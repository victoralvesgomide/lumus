from django.db import models

class Alarm(models.Model):
    hour = models.IntegerField(default=0)
    minute = models.IntegerField(default=0)
    is_enable = models.BooleanField(default=True)
    comment = models.CharField(max_length=500)
    link_video = models.CharField(max_length=500, default='https://www.youtube.com/watch?v=MC64gKvh5R8&t=1s&autoplay=1')