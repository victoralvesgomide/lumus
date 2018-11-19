from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_alarm, name='post_alarm'),
    path('alarms', views.alarms, name='alarms'),
    path('update/<int:id>/', views.update_alarm, name='update_alarm'),
    path('delete/<int:id>/', views.delete_alarm, name='delete_alarm'),
    path('snooze/<int:id>/', views.snooze_alarm, name='snooze_alarm'),
    path('delete_old_alarm/<int:id>/', views.delete_old_alarm, name='delete_old_alarm')
]
