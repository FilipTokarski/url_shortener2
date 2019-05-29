from django.test import TestCase
from .models import UrlModel


class TestModel(TestCase):

    def setUp(self):
        UrlModel.objects.create(original_url='https://www.google.com/')

    def test_model(self):
        url = UrlModel.objects.get(id=1)

        self.assertIsNotNone(UrlModel.objects.all())
        self.assertEqual(url.original_url, 'https://www.google.com/')
