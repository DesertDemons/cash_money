from django.test import TestCase
from django.urls import reverse

class BusinessViewTestCase(TestCase):
    def test_home_view(self):
        list_url = reverse("home")
        response = self.client.get(list_url)
        self.assertIn("Random Business", response.context['title'])
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, "Random Business")
        self.assertEqual(response.status_code, 200)