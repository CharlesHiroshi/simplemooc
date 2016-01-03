from django.core import mail
from django.test import TestCase


class ContactCoursePostValid(TestCase):
    def setUp(self):
        data = dict(name='Charles Hiroshi', email='charles@simplemooc.com',
                    message='Corpo da Mensagem')
        self.response = self.client.post('/courses/contact-course/', data)
        self.email = mail.outbox[0]

    def test_contactCourse_email_subject(self):
        expect = 'Confirmação de Envio'
        self.assertEqual(expect, self.email.subject)

    def test_contactCourse_email_from(self):
        expect = 'contato@simplemooc.org'
        self.assertEqual(expect, self.email.from_email)

    def test_contactCourse_email_to(self):
        expect = ['contato@simplemooc.org', 'charles@simplemooc.com']
        self.assertEqual(expect, self.email.to)

    def test_contactCourse_email_body(self):
        contents = [
            'Charles Hiroshi',
            'charles@simplemooc.com',
            'Corpo da Mensagem',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
