from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>This is HOMEPAGE.</h1>')

def about(request):
    return HttpResponse('<h1>This is ABOUT-PAGE.</h1>')

def contact(request):
    return HttpResponse('<h1>This is CONTACT-PAGE.</h1>')