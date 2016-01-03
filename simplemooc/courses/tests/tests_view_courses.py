from django.core import mail
from django.test import TestCase
from simplemooc.courses.forms import ContactCourseForm


class ContactCourseGet(TestCase):
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
        tags = (('<form', 1),
                ('input', 3),
                ('type="text"', 1),
                ('type="email"', 1),
                ('<textarea', 1),
                ('<button', 1),
                ('type="submit"', 1),
                )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have contact course form"""
        form = self.response.context['form']
        self.assertIsInstance(form, ContactCourseForm)


class ContactCoursePostValid(TestCase):
    def setUp(self):
        data = dict(name='Charles Hiroshi', email='charles@simplemooc.com',
                    message='Corpo da Mensagem')
        self.response = self.client.post('/courses/contact-course/', data)

    def test_post(self):
        """Valid POST should redirect to /contact-course/"""
        self.assertEqual(302, self.response.status_code)

    def test_send_contactCourse_email(self):
        """Valida o envio de email"""
        self.assertEqual(1, len(mail.outbox))


class ContactCoursePostInvalid(TestCase):
    def setUp(self):
        self.response = self.client.post('/courses/contact-course/', {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'courses/contact-course.html')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, ContactCourseForm)

    def test_form_has_errors(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)


class ContactCourseSuccessMessage(TestCase):
    def test_message(self):
        data = dict(name='Charles Hiroshi', email='charles@simplemooc.com',
                    message='Corpo da Mensagem')
        response = self.client.post('/courses/contact-course/', data, follow=True)
        self.assertContains(response, 'E-mail enviado com sucesso!')
