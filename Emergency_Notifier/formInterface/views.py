from django.shortcuts import render

# Create your views here.
def Login(request):
    return render(request,'Html/Login.html')

def Signup(request):
    return render(request,'Html/Signup.html')