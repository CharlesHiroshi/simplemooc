from django.test import TestCase
from simplemooc.courses.forms import ContactCourseForm


class ContactCourseTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/courses/contact-course/')

    def test_get(self):
        """Get /courses/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use courses/contact-course.html"""
        self.assertTemplateUsed(self.response, 'courses/contact-course.html')

    def test_html(self):
        """Html must contain input tags"""
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, 'input', 3)
        self.assertContains(self.response, 'type="text"')
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, '<textarea')
        self.assertContains(self.response, '<button')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have contact course form"""
        form = self.response.context['form']
        self.assertIsInstance(form, ContactCourseForm)

    def test_form_has_fields(self):
        """Form must have 3 fields"""
        form = self.response.context['form']
        self.assertSequenceEqual(['name', 'email', 'message'], list(form.fields))
