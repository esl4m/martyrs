#  views.py
#
#  by: Islam Diaa
#       18 May 2015
#

# from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Martyrs index.")
