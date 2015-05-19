#  urls.py
#
#  by: Islam Diaa
#       18 May 2015
#

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^delete/$', views.delete, name='delete'),
    # url(r'^edit/$', views.edit, name='edit'),
    # url(r'^remove/id/$', views.remove_profile, name='remove'),
]