from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView
from .models import Skills, About, Portfolio

# Create your views here.

class HomePage(TemplateView):
    template_name = 'intro.html'
    
class AboutPage(ListView):
    template_name = 'about.html'
    context_object_name = 'about'
    queryset =  About.objects.all()

class AboutDetailsPage(DetailView):
    model = About
    template_name = 'details.html'
    context_object_name = 'info'
    
class MySkills(ListView):
    template_name = 'skills.html'
    context_object_name = 'skills'
    queryset =  Skills.objects.all()


class PortFolio_View(ListView):
    queryset = Portfolio.objects.all()
    template_name = 'project.html'
    context_object_name = 'projects'

    
    


    
