from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_alarm, name='post_alarm'),
]