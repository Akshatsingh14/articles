from django.shortcuts import render, HttpResponse
from .models import Games

# Create your views here.
details = Games.objects.all()

def display(request):
    context = {
        'article' : details
    }
    return render(request,'index.html', context)

def detail(request, pk):
    data = Games.objects.get(id = pk)
    context = {
        'data' : data
    }
    return render(request,'desc.html',context)