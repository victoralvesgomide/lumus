from django.test import TestCase, Client
from alarm.models import Alarm
from datetime import datetime
from django.urls import reverse
from alarm import views


class AlarmTestCase(TestCase):
    def setUp(self):
        Alarm.objects.create(hour=10, minute=34, is_enable=True,
                             comment='acordar', link_video='video')
        Alarm.objects.create(hour=10, minute=34, is_enable=False,
                             comment='nao_acordar', link_video='video2')

    def test_alarm_get(self):
        """
        Test method get to alarm model
        """
        test = Alarm.objects.get(is_enable=False)
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
        self.assertEqual(test.is_enable, views.get_alarm_by_id(1).is_enable)

    def test_get_next_alarm(self):
        """
        Test if the method returns a array ordened
        """
        test = views.get_next_alarm()
        self.assertEqual(True, (test, '__len__')
                         and (not isinstance(test, str)))

    def test_snooze_model_method(self):
        """
        Test if the method increments 10 minutes
        """
        test = Alarm.objects.create(
            hour=10, minute=34, is_enable=True, comment='acordar', link_video='video')
        test.alarm_snooze()
        self.assertEqual(test.minute == 44, True)
        test = Alarm.objects.create(
            hour=23, minute=51, is_enable=True, comment='acordar', link_video='video')
        test.alarm_snooze()
        self.assertEqual(test.minute == 1, True)


class RequestPageTestCase(TestCase):

    def setUp(self):
        Alarm.objects.create(hour=10, minute=34, is_enable=True,
                             comment='acordar', link_video='video')
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

    def test_alarm_page_form(self):
        url = reverse('alarms')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alarm/alarm.html')

    def test_delete_alarm_post(self):
        url = reverse('delete_alarm', args=[1])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
    
    def test_delete_alarm_get(self):
        url = reverse('delete_alarm', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_alarm_post(self):
        url = reverse('update_alarm', args=[1])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alarm/alarm.html')

    def test_update_alarm_get(self):
        url = reverse('update_alarm', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alarm/alarm.html')

    def test_delete_old_alarm(self):
        url = reverse('delete_old_alarm', args=[1])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)

    def test_snooze_alarm(self):
        url = reverse('snooze_alarm', args=[1])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
