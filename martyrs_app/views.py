#  views.py
#
#  by: Islam Diaa
#       18 May 2015
#

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from .models import MartyrsProfile


def index(request):
    res_list = MartyrsProfile.objects.order_by('name')
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'res_list': res_list,
    })
    return HttpResponse(template.render(context))


def add(request):
    new_case = MartyrsProfile(name=request.POST['name'],
                              date_of_birth=request.POST['date_of_birth'],
                              date_of_death=request.POST['date_of_death'],
                              cause_of_death=request.POST['cause_of_death'],
                              officer_name=request.POST['officer_name'],
                              governorate=request.POST['governorate'])
    new_case.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request):
    case_id = request.POST.get('id')
    MartyrsProfile.objects.filter(id=case_id).delete()
    
    # case = MartyrsProfile.objects.get(id=request.POST.get['id'])
    # case.delete()

    return HttpResponseRedirect(reverse('index'))


# def edit(request):
#     case = MartyrsProfile.objects.get(id=request.POST['id'])
#     if request.POST['submitButton'] == 'Update':
#         case.name = request.POST['name']
#         case.date_of_birth = request.POST['date_of_birth']
#         case.date_of_death = request.POST['date_of_death']
#         case.cause_of_death = request.POST['cause_of_death']
#         case.officer_name = request.POST['officer_name']
#         case.governorate = request.POST['governorate']
#         case.save()
#
#     elif request.POST['submitButton'] == 'Delete':
#         case.delete()
#
#     return HttpResponseRedirect(reverse('index'))

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