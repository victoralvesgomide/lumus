from django.test import TestCase, Client
from alarm.models import Alarm
from datetime import datetime
from django.urls import reverse
from alarm import views


class AlarmTestCase(TestCase):
    def setUp(self):
        date = datetime.now()
        Alarm.objects.create(time=date.time(), status='OPEN', comment='acordar', link_video='video')
        Alarm.objects.create(time=date.time(), status='CLOSE', comment='nao_acordar', link_video='video2')

    def test_alarm_get(self):
        """
        Test method get to alarm model
        """
        test = Alarm.objects.get(status='CLOSE')
        self.assertEqual(test.comment, 'nao_acordar')

    def test_get_all_alarm(self):
        """
        Test if the function returns all objects
        """
        test = Alarm.objects.all().count()
        self.assertEqual(test, views.get_all_alarm().count())

    def test_get_alarm_by_id(self):
        """
        Test if the method returns a object by id
        """
        test = Alarm.objects.get(id=1)
        self.assertEqual(test.status, views.get_alarm_by_id(1).status)

"""
class RequestPageTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        url = reverse('post_alarm')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alarm/home.html')

    def test_alarm_page(self):
        url = reverse('alarms')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alarm/alarm.html')
        
    def test_create_alarm(self):
        url = reverse('create_alarm')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alarm/create_alarm.html')
        
    def test_delete_alarm(self):
        url = reverse('delete_alarm')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alarm/delete_alarm.html')

    def test_update_alarm(self):
        url = reverse('update_alarm')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alarm/update_alarm.html')"""