from django.conf.urls import url
from . import views


urlpatterns = [
            url(r'^$', views.index, name='index'),
            url(r'^active-members/$', views.active_members, name='active_members'),
            url(r'^about/$', views.about, name='about'),
            ]
