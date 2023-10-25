from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

# Create your views here.
class Home(generic.TemplateView):
    template_name='bases/home.html'

class WebApps(generic.TemplateView):
    template_name='bases/web_apps.html'

class WebDevelopment(generic.TemplateView):
    template_name='bases/web_development.html'
