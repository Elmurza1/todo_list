from django.test import TestCase
from .views import *
# Create your tests here.

class TestDashboardPage(TestCase):
    def test_home_success(self):
        response = self.client.get('/dashboard-page/')
        self.assertEqual(response.status_code, 200)
