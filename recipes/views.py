from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse('HOME PAGE 1')

def contato(request):
    return HttpResponse('PÁGINA DE CONTATO')

def sobre(request):
    return HttpResponse('SOBRE')