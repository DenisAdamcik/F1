from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Driver, Team, Car


def index(request):
    drivers = Driver.objects.all()
    teams = Team.objects.all()
    cars = Car.objects.all()
    return render(request, 'index.html', {
        'drivers': drivers,
        'teams': teams,
        'cars': cars
    })

class DriverListView(ListView):
    model = Driver
    template_name = 'drivers/driver_list.html'
    context_object_name = 'drivers'


class DriverDetailView(DetailView):
    model = Driver
    template_name = 'drivers/driver_detail.html'
    context_object_name = 'driver'


class DriverCreateView(CreateView):
    model = Driver
    template_name = 'drivers/driver_form.html'

    def get_success_url(self):
        return reverse_lazy('driver_detail', kwargs={'pk': self.object.pk})


class DriverUpdateView(UpdateView):
    model = Driver
    template_name = 'drivers/driver_form.html'
    context_object_name = 'driver'

    def get_success_url(self):
        return reverse_lazy('driver_detail', kwargs={'pk': self.object.pk})


class DriverDeleteView(DeleteView):
    model = Driver
    template_name = 'drivers/driver_confirm_delete.html'
    context_object_name = 'driver'
    success_url = reverse_lazy('driver_list')



class TeamListView(ListView):
    model = Team
    template_name = 'teams/team_list.html'
    context_object_name = 'teams'


class TeamDetailView(DetailView):
    model = Team
    template_name = 'teams/team_detail.html'
    context_object_name = 'team'


class TeamCreateView(CreateView):
    model = Team
    template_name = 'teams/team_form.html'

    def get_success_url(self):
        return reverse_lazy('team_detail', kwargs={'pk': self.object.pk})


class TeamUpdateView(UpdateView):
    model = Team
    template_name = 'teams/team_form.html'
    context_object_name = 'team'

    def get_success_url(self):
        return reverse_lazy('team_detail', kwargs={'pk': self.object.pk})


class TeamDeleteView(DeleteView):
    model = Team
    template_name = 'teams/team_confirm_delete.html'
    context_object_name = 'team'
    success_url = reverse_lazy('team_list')

class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'
    context_object_name = 'cars'


class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'
    context_object_name = 'car'


class CarCreateView(CreateView):
    model = Car
    template_name = 'cars/car_form.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'cars/car_form.html'
    context_object_name = 'car'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'cars/car_confirm_delete.html'
    context_object_name = 'car'
    success_url = reverse_lazy('car_list')
