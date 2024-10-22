from django.shortcuts import render
from django.views.generic import TemplateView



class HomeView(TemplateView):
    template_name = 'pages/home.html'

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class ReservationView(TemplateView):
    template_name = 'pages/reservation.html'

class DealsView(TemplateView):
    template_name = 'pages/deals.html'


class RegisterView(TemplateView):
    template_name = 'pages/register.html'













