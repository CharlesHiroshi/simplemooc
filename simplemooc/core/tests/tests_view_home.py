from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')
        self.response_contact = self.client.get('/contact/')

    def test_get(self):
        """GET / Must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use home.html"""
        self.assertTemplateUsed(self.response, 'home.html')

    def test_ContactCourse(self):
        self.assertContains(self.response_contact, 'href="/courses/contact-course/"')
