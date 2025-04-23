from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def vegetables(request):
    return HttpResponse('vegetables')