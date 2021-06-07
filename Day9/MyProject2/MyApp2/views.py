from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def success(request):
    fstname = request.POST['fname']
    lstname = request.POST['lname']
    usrname = request.POST['uname']
    Email = request.POST['mail']
    return render(request,'done.html',{'fname':fstname,'lname':lstname,'uname':usrname,'email':Email})