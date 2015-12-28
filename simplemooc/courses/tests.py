from django.test import TestCase


class ContactCourseTest(TestCase):
    def test_get(self):
        """Get /courses/ must return status code 200"""
        response = self.client.get('/courses/contact-course/')
        self.assertEqual(200, response.status_code)

    def test_template(self):
        """Must use courses/contact-course.html"""
        response = self.client.get('/courses/contact-course/')
        self.assertTemplateUsed(response, 'courses/contact-course.html')
