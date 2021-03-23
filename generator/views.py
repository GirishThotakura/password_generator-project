from django.shortcuts import render, redirect
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()~"{}'))

    the_password = ''

    for i in range(length):
        the_password += random.choice(characters)
    return render(request, 'generator/password.html', {'pass': the_password})


def about(request):
    return render(request, 'generator/about.html')
