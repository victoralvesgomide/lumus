from django.db import models
import datetime as dt
from django.core.validators import MaxValueValidator, MinValueValidator


class Alarm(models.Model):
    hour = models.IntegerField(default=0, choices=((x, "{:02}".format(x)) for x in range(0,24)))
    minute = models.IntegerField(default=0, choices=((x, "{:02}".format(x)) for x in range(0,60)))
    is_enable = models.BooleanField(default=True)
    comment = models.CharField(max_length=500)
    link_video = models.CharField(
        max_length=500, default='https://www.youtube.com/watch?v=MC64gKvh5R8')

    def alarm_snooze(self):
        self.minute += 10
        if(self.minute >= 60):
            self.minute -= 60
            self.hour += 1
            if(self.hour >= 24):
              self.hour = self.hour - 24
        self.save()