from django.test import TestCase

# Create your tests here.
class RegisterTestCase(TestCase):
    def test_register_success(self):
        response = self.client.get('/register-page/')
        self.assertEqual(response.status_code, 200)