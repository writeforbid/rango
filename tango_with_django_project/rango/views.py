from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context_dict = {'boldmessage':"I am bold from the context"}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    return HttpResponse("<a href=/rango/>I'm about</a>")