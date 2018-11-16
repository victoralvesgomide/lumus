from django.db import models
import datetime as dt


class Alarm(models.Model):
    hour = models.IntegerField(default=0)
    minute = models.IntegerField(default=0)
    is_enable = models.BooleanField(default=True)
    comment = models.CharField(max_length=500)
    link_video = models.CharField(max_length=500, default='https://www.youtube.com/watch?v=MC64gKvh5R8&t=1s&autoplay=1')

    # def alarm_snooze(self):
    #     now = self.time
    #     delta = dt.timedelta(minutes=10)
    #     t = now
    #     self.time = (dt.datetime.combine(dt.date(1, 1, 1), t) + delta).time()
    #     self.save()
