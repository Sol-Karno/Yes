from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import *

class ServiceList(ListView):
    model = Service

class ServiceCreate(CreateView):
    model = Service
    fields = ['title', 'price']
    success_url = reverse_lazy('service_cbv:service_list')

class ServiceUpdate(UpdateView):
    model = Service
    fields = ['title', 'price']
    success_url = reverse_lazy('service_cbv:service_list')

class ServiceDelete(DeleteView):
    model = Service
    success_url = reverse_lazy('service_cbv:service_list')