from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_alarm, name='post_alarm'),
    path('alarms', views.alarms, name='alarms'),
    path('create_alarm', views.create_alarm, name='create_alarm'),
    #path('update/<int:id>/', views.update_alarm, 'update_alarm'),
    #path('delete/<int:id>/', views.delete_alarm, 'delete_alarm')
]
