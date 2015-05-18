from django.contrib import admin
from .models import MartyrsProfile


class MartyrsProfileAdmin(admin.ModelAdmin):
    fields = ['name', 'date_of_birth', 'date_of_death', 'cause_of_death', 'officer_name', 'governorate']

admin.site.register(MartyrsProfile)