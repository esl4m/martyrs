from django.db import models


class MartyrsProfile(models.Model):
    name = models.CharField(max_length=128, null=True)
    date_of_birth = models.DateTimeField()
    date_of_death = models.DateTimeField()
    cause_of_death = models.CharField(max_length=128, null=True, blank=True)
    officer_name = models.CharField(max_length=128, null=True, blank=True)
    governorate = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        db_table = 'MartyrsProfile'
