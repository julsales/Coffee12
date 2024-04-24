from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def Homepage(request):
    return render(request, 'homepage.html')  # Renderiza o template "homepage.html"

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Sua senha está diferente da confirmação")
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')
        

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            return HttpResponse("Nome de usuário ou senha incongruentes")
    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def SignupCafePage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Sua senha está diferente da confirmação")
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')
        

    return render(request, 'signupCafe.html')
