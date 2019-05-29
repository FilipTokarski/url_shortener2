#from django import status_code
from django.test import Client, TestCase
from django.urls import reverse

from .models import UrlModel
from .utils import generate_random_string


class TestModel(TestCase):

    def setUp(self):
        UrlModel.objects.create(original_url='https://www.google.com/')

    def test_generate_random_string(self):
        data = generate_random_string()

        self.assertEqual(type(data), str)
        self.assertTrue(data.isalnum())
        self.assertEqual(len(data), 8)

    def test_model(self):
        url = UrlModel.objects.get(id=1)

        self.assertIsNotNone(UrlModel.objects.all())
        self.assertIsNotNone(url.url_slug)
        self.assertEqual(url.original_url, 'https://www.google.com/')
        self.assertTrue(url.shortened_url.startswith('https://ftdevprojects.pl/'))
        self.assertTrue(url.date_added)


class TestViews(TestCase):

    def test_get_create_url_view(self):
        client = Client()
        response = client.get(reverse('create-url'))

        self.assertEqual(response.status_code, 200)

    def test_post_create_url_view(self):
        client = Client()
        response = client.post(reverse('create-url'),
                                 {'original_url': 'https://www.google.com/'})

        self.assertEqual(response.status_code, 200)

    def test_redirect_view(self):
        pass
