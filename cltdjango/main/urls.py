from django.conf.urls import url
from . import views


urlpatterns = [
            url(r'^$', views.index, name='index'),
            url(r'^active_members/$', views.active_members, name='active_members'),
            ]
