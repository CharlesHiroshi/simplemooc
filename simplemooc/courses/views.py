from django.shortcuts import render
from simplemooc.courses.forms import ContactCourseForm


def contactCourse(request):
    context = {'form': ContactCourseForm()}
    return render(request, 'courses/contact-course.html', context)
