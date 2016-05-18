from django.conf.urls import include, url
# from django.contrib.auth import views as django_views

from . import views


urlpatterns = [

    url(r'^api/polygon/$', views.PolygonAddressListCreate.as_view()),
    url(r'^api/polygon/(?P<id>[0-9]+)/$', views.PolygonAddressDetail.as_view()),
    # url(r'^api/polygon/filter/', views.PolygonAddressFilter),
]
