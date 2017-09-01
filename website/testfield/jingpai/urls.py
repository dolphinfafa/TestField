from django.conf.urls import patterns, url
from jingpai import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'))