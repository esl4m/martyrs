#  urls.py
#
#  by: Islam Diaa
#       18 May 2015
#

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^martyrs_app/', include('martyrs_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
