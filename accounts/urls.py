from django.conf.urls import include, url
# from django.contrib.auth import views as django_views

from . import views


urlpatterns = [

    url(r'^api/transporter/$', views.TransportOperatorListCreate.as_view()),
    url(r'^api/transporter/(?P<id>[0-9]+)/$', views.TransportOperatorDetail.as_view()),
]
