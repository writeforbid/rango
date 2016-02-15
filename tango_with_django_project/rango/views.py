from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context_dict = {'boldmessage':"I am bold from the context"}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_dict = {'aboutmessage':"I am from aboutmessage"}
    return render(request,'rango/about.html', context_dict)