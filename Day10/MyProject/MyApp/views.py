from MyApp.models import Student
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Student

# Create your views here.
def index(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
    
class studentlist(ListView):
    model = Student
    template_name = 'slist.html'