from django.conf.urls import patterns, url
from sentiment import views

urlpatterns = patterns('',
        url(r'^sentence/$', views.sententce, name='sentence'),)