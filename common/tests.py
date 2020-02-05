from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'TDE Central')
