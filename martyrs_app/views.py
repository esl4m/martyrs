#  views.py
#
#  by: Islam Diaa
#       18 May 2015
#

from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import MartyrsProfile


def index(request):
    res_list = MartyrsProfile.objects.order_by('name')
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'res_list': res_list,
    })
    return HttpResponse(template.render(context))

#
# def remove_profile(request):
#     id = request.POST.get('id')
#     MartyrsProfile.objects.filter(id=id).delete()
#     template = loader.get_template('index.html')
#     response = {
#         'error': False,
#         'error_message': ''
#     }
#     return HttpResponse(template.render(response))