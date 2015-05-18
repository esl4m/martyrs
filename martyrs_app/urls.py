#  urls.py
#
#  by: Islam Diaa
#       18 May 2015
#

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]