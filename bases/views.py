from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from .models import Contact
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.
class Home(generic.TemplateView):
    template_name='bases/home.html'

class WebApps(generic.TemplateView):
    template_name='bases/web_apps.html'

class WebDevelopment(generic.TemplateView):
    template_name='bases/web_development.html'

class ContactView(SuccessMessageMixin, generic.CreateView):
    template_name='bases/contact.html'
    model=Contact
    context_object_name='obj'
    form_class= ContactForm
    success_url = reverse_lazy("bases:contact")
    success_message='Te haz registrado correctamente'

    def form_valid(self, form):
        return super().form_valid(form)