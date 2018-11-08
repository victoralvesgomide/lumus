from django.test import TestCase

class TestCaseExample(TestCase):

    def test_animals_can_speak(self):
        """Example of test"""
        self.assertEqual('Example of test', 'Example of test')