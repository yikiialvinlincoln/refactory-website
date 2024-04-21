from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def loginView(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def registerView(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())

def forgotView(request):
    template = loader.get_template('forgot.html')
    return HttpResponse(template.render())