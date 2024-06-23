from django.shortcuts import render,HttpResponse
from aalu.models import Review1
from aalu.models import Signin
from aalu.models import Login
from aalu.models import UserRev
def index(request):

    return render(request,'index.html')

def review1(request):
    if request.method=='POST':
        
        search=request.POST.get('search')
        review1=Review1(name=name,comment=comment)
        review1.save()
        return render(request,'review1.html')
    return render(request,'review1.html')
def signin(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        paasword=request.POST.get('password')
        signin=Signin(name=name,email=email,password='password')
        signin.save()
    return render(request,'signin.html')
def login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        
        password=request.POST.get('password')
        login=Login(name=name,password='password')
        login.save()
    return render(request,'login.html') 
def userRev(request):
    if request.method=='POST':
        name=request.POST.get('name')
        movie=request.POST.get('movie')
       # review=request.POST.get('review')
        userRev=UserRev(name=name,movie=movie,review=review)
        userRev.save()
        return render(request,'userRev.html')
    return render(request,'userRev.html')           
  