from django.shortcuts import render


def contactCourse(request):
    return render(request, 'courses/contact-course.html')
