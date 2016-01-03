from django.test import TestCase
from simplemooc.courses.forms import ContactCourseForm


class ContactCourseFormTest(TestCase):
    def setUp(self):
        self.form = ContactCourseForm()


    def test_form_has_fields(self):
        """Form must have 3 fields"""
        expected = ['name', 'email', 'message']
        self.assertSequenceEqual(expected, list(self.form.fields))
