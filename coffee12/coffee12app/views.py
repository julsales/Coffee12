from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Estabelecimento


@login_required(login_url='login')
def Homepage(request):
    return render(request, 'homepage.html')  # Renderiza o template "homepage.html"

@login_required(login_url='login')
def HomepageCafe(request):
    context = {
        'possui_estabelecimento': request.user.possui_estabelecimento
    }
    return render(request, 'homepagecafe.html', context)  # Renderiza o template "homepage.html"

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        phone_number = request.POST.get('phone_number')
        if pass1 != pass2:
            return HttpResponse("Sua senha está diferente da confirmação")
        my_user = CustomUser.objects.create_user(username=uname, email=email, password=pass1)
        my_user.phone_number = phone_number
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
            if user.role == 'CL':
                return redirect('homepage')
            if user.role == 'CM':
                return redirect('homepagecafe')
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
        phone_number = request.POST.get('phone_number')
        if pass1!=pass2:
            return HttpResponse("Sua senha está diferente da confirmação")
        my_user=CustomUser.objects.create_user(username=uname, email=email, password=pass1,role='CM')
        my_user.phone_number = phone_number
        my_user.save()
        return redirect('login')
        

    return render(request, 'signupCafe.html')

def CadastrarEstabelecimento(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        proprietario = request.user
        estabelecimento = Estabelecimento.objects.create(nome=nome, endereco=endereco, telefone=telefone, proprietario=proprietario)
        estabelecimento.save()
        request.user.possui_estabelecimento = True
        request.user.cafeteria = estabelecimento
        
        request.user.save()

        return redirect('homepagecafe')
    return render(request, 'cadastrarEstabelecimento.html')

def EditarEstabelecimento(request):
    if request.method =='POST':
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        proprietario = request.user
        estabelecimento = Estabelecimento.objects.get(proprietario=proprietario)
        estabelecimento.nome = nome
        estabelecimento.endereco = endereco
        estabelecimento.telefone = telefone
        estabelecimento.save()
        return redirect('homepagecafe')
    return render(request, 'editarEstabelecimento.html')

def ExcluirEstabelecimento(request):
    proprietario = request.user
    estabelecimento = Estabelecimento.objects.get(proprietario=proprietario)
    request.user.cafeteria = None
    request.user.possui_estabelecimento = False
    request.user.save()
    estabelecimento.delete()
    
    return redirect('homepagecafe')
