from django.conf.urls import url
from simplemooc.core.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
]
