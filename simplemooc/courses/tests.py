from django.core import mail
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


class ContactCoursePostTest(TestCase):
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

    def test_contactCourse_email_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmação de Envio'
        self.assertEqual(expect, email.subject)

    def test_contactCourse_email_from(self):
        email = mail.outbox[0]
        expect = 'contato@simplemooc.org'
        self.assertEqual(expect, email.from_email)

    def test_contactCourse_email_to(self):
        email = mail.outbox[0]
        expect = ['contato@simplemooc.org', 'charles@simplemooc.com']
        self.assertEqual(expect, email.to)

    def test_contactCourse_email_body(self):
        email = mail.outbox[0]
        self.assertIn('Charles Hiroshi', email.body)
        self.assertIn('charles@simplemooc.com', email.body)
        self.assertIn('Corpo da Mensagem', email.body)


class ContactCourseInvalidPost(TestCase):
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
