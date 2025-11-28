from django.test import TestCase, Client
from django.urls import reverse
from .models import Module

class SimplePagesTest(TestCase):
    def setUp(self):
        self.client = Client()
        # buat beberapa module dummy untuk test listing
        Module.objects.create(slug='linux-dasar', title='Linux Dasar', order=1)
        Module.objects.create(slug='distro-linux', title='Distro Linux', order=2)

    def test_index_status(self):
        resp = self.client.get(reverse('pembelajaran:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Belajar Linux")

    def test_pages_exist(self):
        pages = [
            'pembelajaran:linux_dasar',
            'pembelajaran:belajar_linux',
            'pembelajaran:install_linux',
        ]
        for p in pages:
            resp = self.client.get(reverse(p))
            self.assertEqual(resp.status_code, 200)
