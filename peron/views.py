from django.shortcuts import render
from .models import Station, Line
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .forms import AddForm
from django.http import HttpResponse
from django.contrib import admin
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from django.core.paginator import Paginator



class LineList(ListView):
    paginate_by = 5 
    model = Line

class LineCreate(CreateView):
    model = Line
    fields = "__all__"
    template_name = 'peron/line_add.html'
    success_url = '/line/'

class LineEdit(UpdateView):
    model = Line
    fields = "__all__"
    template_name = 'peron/line_edit.html'
    success_url = '/line/'

class LineDelete(DeleteView):
    model = Line
    success_url = '/line/'
  

class StationList(ListView):
    paginate_by = 5 
    model = Station
    

class StationCreate(CreateView):
    model = Station
    fields = "__all__"
    template_name = 'peron/station_add.html'
    success_url = '/station/'

class StationEdit(UpdateView):
    model = Station
    fields = "__all__"
    template_name = 'peron/station_edit.html'
    success_url = '/station/'

class StationDelete(DeleteView):
    model = Station
    success_url = '/station/'


def map(request):
    return render(request, 'peron/map.html')

def home(request):
    return render(request, 'peron/home.html')