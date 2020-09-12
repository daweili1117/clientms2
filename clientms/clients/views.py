from django.contrib.auth.mixins import LoginRequiredMixin  # New
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from .models import Client, Comment, Vehicle
from django.urls import reverse_lazy

from django.core.mail import send_mail


# Client view
class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client_list.html'


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'client_detail.html'
    login_url = 'login'


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    template_name = 'client_edit.html'


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'client_new.html'
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    login_url = 'login'


#
# Vehicle View

class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'


class VehicleDetailView(LoginRequiredMixin, DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'
    login_url = 'login'


class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicle
    fields = ('client', 'make', 'model', 'VIN', 'DatePurchase', 'LastService')
    template_name = 'vehicle_edit.html'


class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehicle
    template_name = 'vehicle_delete.html'
    success_url = reverse_lazy('vehicle_list')


class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    template_name = 'vehicle_new.html'
    fields = ('client', 'make', 'model', 'VIN', 'DatePurchase', 'LastService')
    login_url = 'login'



def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
