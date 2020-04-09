from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'cnjeevbve',})

def password(request):
    up=True
    sp=False
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('@!#$%ˆ&*'))

    if request.GET.get('numbers'):
        characters.extend(list('123456789'))

    length=int(request.GET.get('length', 12))

    thepassword=''
    for x in range(length):
        thepassword+=random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword, 'characters':characters})

def about (request):
    return render(request, 'generator/about.html')
