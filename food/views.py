from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def biryani(request):
    return HttpResponse('Briyani')
def icecream(request):
    return HttpResponse('Amul icecreams')
