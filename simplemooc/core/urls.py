from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'simplemooc.core.views.home', name='home'),
]
