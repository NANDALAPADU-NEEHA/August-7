from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def home(request):
    return render(request,'home.html')

def loginv(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method=='POST':
        a=request.POST.get('kname')
        b=request.POST.get('kpass')
        print(a,b)
        result=authenticate(request,username=a,password=b)
        if result is not None:
            login(request,result)
            if request.user.is_superuser:
               return redirect('/admin')
            else:
               return redirect('loginpage')    
    return render(request,'login.html')

def register(request):
    if request.method=="POST":
        c=request.POST.get('uname')
        d=request.POST.get('fname')
        e=request.POST.get('lname')
        f=request.POST.get('mail')
        g=request.POST.get('passw')
        h=request.POST.get('cpass')
        print(c,d,e,f,g,h)
        result=authenticate(request,username=c,firstname=d,lastname=e)
        if result is not None:
            register(request,result)
    return render(request,'register.html')

def create(request):
    return render(request,'create.html')

def profile(request):
    return render(request,'profile.html')

def logoutv(request):
    return redirect('loginpage')
