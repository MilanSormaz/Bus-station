from django.db import models
from datetime import date
import django_tables2 as tables

class Station(models.Model):

    name = models.CharField(max_length=200, blank = False)
    create_at = models.DateField(auto_now_add=True, blank=False)
    note = models.TextField(blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank = False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank = False)


    def __str__(self):
        return self.name



class Line(models.Model):

    name = models.CharField(max_length=200, blank=False)
    start = models.ForeignKey('Station', on_delete=models.CASCADE, null=False, blank=False, related_name='start')
    middle = models.ForeignKey('Station', on_delete=models.CASCADE, null=False, blank=False, related_name='middle')
    end = models.ForeignKey('Station', on_delete=models.CASCADE, null=False, blank=False, related_name='end')
    create_at = models.DateField(auto_now_add=True, blank=False)
    note = models.TextField(blank=True)
    night_line = models.BooleanField(default=False)

    def __str__(self):
        return self.name