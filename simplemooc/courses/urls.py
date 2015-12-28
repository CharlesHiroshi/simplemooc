from django.conf.urls import url
from simplemooc.courses.views import contactCourse

urlpatterns = [
    url(r'^contact-course/$', contactCourse, name='contactCourse'),
]