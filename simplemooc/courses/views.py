from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from simplemooc.courses.forms import ContactCourseForm


def contactCourse(request):
    if request.method == 'POST':
        form = ContactCourseForm(request.POST)
        if form.is_valid():
            body = render_to_string('courses/contact-course-email.txt', form.cleaned_data)
            mail.send_mail('Confirmação de Envio',
                           body,
                           'contato@simplemooc.org',
                           ['contato@simplemooc.org', form.cleaned_data['email']])
            messages.success(request, 'E-mail enviado com sucesso!')
            return HttpResponseRedirect('/courses/contact-course/')
        else:
            return render(request, 'courses/contact-course.html', {'form': form})
    else:
        context = {'form': ContactCourseForm()}
        return render(request, 'courses/contact-course.html', context)
