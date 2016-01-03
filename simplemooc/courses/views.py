from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from simplemooc.courses.forms import ContactCourseForm


def contactCourse(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def create(request):
    form = ContactCourseForm(request.POST)
    if not form.is_valid():
        return render(request, 'courses/contact-course.html', {'form': form})
    _send_mail('Confirmação de Envio',
               settings.DEFAULT_FROM_EMAIL,
               form.cleaned_data['email'],
               'courses/contact-course-email.txt',
               form.cleaned_data)
    messages.success(request, 'E-mail enviado com sucesso!')
    return HttpResponseRedirect('/courses/contact-course/')


def new(request):
    return render(request, 'courses/contact-course.html', {'form': ContactCourseForm()})


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])