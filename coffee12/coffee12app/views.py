from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Estabelecimento, Prato
from django.shortcuts import get_object_or_404



@login_required(login_url='login')
def Homepage(request):
    estabelecimentos = Estabelecimento.objects.all()
    pratos = Prato.objects.all()
    context = {
        'possui_estabelecimento': request.user.possui_estabelecimento,
        'cafeteria_nome': request.user.cafeteria.nome if request.user.possui_estabelecimento else None,
        'estabelecimentos': estabelecimentos,
        'pratos': pratos
    }
    return render(request, 'homepage.html', context)

@login_required(login_url='login')
def HomepageCafe(request):
    
    context = {
        'possui_estabelecimento': request.user.possui_estabelecimento,
        'cafeteria_nome': request.user.cafeteria.nome if request.user.possui_estabelecimento else None,
        'pratos': Prato.objects.filter(estabelecimento=request.user.cafeteria) if request.user.possui_estabelecimento else None
    }
    return render(request, 'homepagecafe.html', context)

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

def CadastrarPrato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        preco_promocional = request.POST.get('preco_promocional')
        prato_principal = 'prato_principal' in request.POST
        estabelecimento = request.user.cafeteria
        prato = Prato.objects.create(nome=nome, descricao=descricao, preco=preco, preco_promocional=preco_promocional,prato_principal=prato_principal, estabelecimento=estabelecimento)
        prato.save()
        return redirect('homepagecafe')
    return render(request, 'cadastrarPrato.html')



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
    estabelecimentos = Estabelecimento.objects.filter(proprietario=proprietario)
    request.user.cafeteria = None
    request.user.possui_estabelecimento = False
    request.user.save()
    estabelecimentos.delete()
    
    return redirect('homepagecafe')


def ExcluirPrato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        estabelecimento = request.user.cafeteria
        prato = Prato.objects.get(nome=nome, estabelecimento=estabelecimento)
        prato.delete()
        return redirect('homepagecafe')
    return render(request, 'excluirPrato.html')

def Inicio(request):
    return render(request, 'inicio.html')

@login_required(login_url='login')
def FavoritarCafeteria(request, id):
    id_cafeteria = request.POST.get('id_cafeteria')
    cafeteria = get_object_or_404(Estabelecimento, id=id_cafeteria)   
    if request.method == 'POST':
        cafeteria = Estabelecimento.objects.get(id=id_cafeteria)
        request.user.cafeteria_favorita.add(cafeteria)
        request.user.save()
    # Obter a URL da página anterior
    previous_page = request.META.get('HTTP_REFERER')

    # Redirecionar para a página anterior
    return HttpResponseRedirect(previous_page)

from django.http import HttpResponseRedirect
from django.http import Http404

def DesfavoritarCafeteria(request, id):
    if request.method == 'POST':
        cafeteria = get_object_or_404(Estabelecimento, id=id)
        request.user.cafeteria_favorita.remove(cafeteria)
        request.user.save()

        # Get the URL of the previous page
        previous_page = request.META.get('HTTP_REFERER', '/')

        # Redirect to the previous page
        return HttpResponseRedirect(previous_page)

    raise Http404("Invalid request method")

def VerCafeteriasFavoritas(request):
    context = {
        'cafeterias_favoritas': request.user.cafeteria_favorita.all()
    }
    return render(request, 'verCafeteriasFavoritas.html', context)

def Favoritos(request):
    context = {
        'cafeterias_favoritas': request.user.cafeteria_favorita.all()
    }
    return render(request, 'favoritos.html', context)

def PerfilCafeteria(request, id_cafeteria):
    estabelecimento = Estabelecimento.objects.get(id=id_cafeteria)
    cardapio = Prato.objects.filter(estabelecimento=estabelecimento)
    return render(request, 'perfilCafeteria.html', {'estabelecimento': estabelecimento, 'cardapio': cardapio})
    
