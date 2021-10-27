from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, You're at the home page.")

def recipes(request):
    return HttpResponse("Hello, You're at the recipes page.")