from re import template
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):

    template_name = 'landing.html'
    title = 'Heladeria Resistire'


    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = self.title

        return context