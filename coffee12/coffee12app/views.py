from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Estabelecimento, Prato
from django.shortcuts import get_object_or_404
from .models import Feedback
from .models import Historico
from .models import Reserva
from .models import ItemEsquecido
from .forms import FeedbackForm
from .forms import ReservaForm



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
    cafeteria = request.user.cafeteria if request.user.possui_estabelecimento else None
    rating_average = cafeteria.rating_average
    context = {
        'possui_estabelecimento': request.user.possui_estabelecimento,
        'cafeteria': cafeteria,
        'pratos': Prato.objects.filter(estabelecimento=cafeteria) if cafeteria else None,
        'rating_average': rating_average 
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
        try:
            existing_user = CustomUser.objects.get(username=uname)
            return HttpResponse("Nome de usuário já existe")
        except CustomUser.DoesNotExist:
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
        try:
            existing_user = CustomUser.objects.get(username=uname)
            return HttpResponse("Nome de usuário já existe")
        except CustomUser.DoesNotExist:
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
    cafeteria = Estabelecimento.objects.get(proprietario=request.user)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        preco_promocional = request.POST.get('preco_promocional')
        prato_principal = 'prato_principal' in request.POST
        
        prato = Prato.objects.create(nome=nome, descricao=descricao, preco=preco, preco_promocional=preco_promocional,prato_principal=prato_principal, estabelecimento=cafeteria)
        prato.save()
        return redirect('homepagecafe')
    return render(request, 'cadastrarPrato.html',{'estabelecimento': cafeteria,'possui_estabelecimento': request.user.possui_estabelecimento,})


def EditarEstabelecimento(request):
    cafeteria = Estabelecimento.objects.get(proprietario=request.user)
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
    return render(request, 'editarEstabelecimento.html',{'estabelecimento': cafeteria,'possui_estabelecimento': request.user.possui_estabelecimento,})

def ExcluirEstabelecimento(request):
    proprietario = request.user
    estabelecimentos = Estabelecimento.objects.filter(proprietario=proprietario)
    request.user.cafeteria = None
    request.user.possui_estabelecimento = False
    request.user.save()
    estabelecimentos.delete()
    
    return redirect('homepagecafe')


def ExcluirPrato(request):
    cafeteria = Estabelecimento.objects.get(proprietario=request.user)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        estabelecimento = request.user.cafeteria
        prato = Prato.objects.get(nome=nome, estabelecimento=estabelecimento)
        prato.delete()
        return redirect('homepagecafe')
    return render(request, 'excluirPrato.html',{'estabelecimento': cafeteria,'possui_estabelecimento': request.user.possui_estabelecimento,})
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
    rating_average = estabelecimento.rating_average
    return render(request, 'perfilcafeteria.html', {'estabelecimento': estabelecimento, 'cardapio': cardapio, 'rating_average': rating_average})

def feedback(request, id):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.cafeteria = get_object_or_404(Estabelecimento, id=id)
            feedback.save()
            return redirect('perfilCafeteria', id_cafeteria=id)
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def VerFeedbacks(request, id_cafeteria):
    estabelecimento = Estabelecimento.objects.get(id=id_cafeteria)
    feedbacks = Feedback.objects.filter(cafeteria=estabelecimento).order_by('-created_at')[:10]
    return render(request, 'verFeedbacks.html', { 'feedbacks': feedbacks,'estabelecimento': estabelecimento,'possui_estabelecimento': request.user.possui_estabelecimento,})

def add_to_historico(request, cafeteria_id):
    Historico.objects.create(user=request.user, cafeteria_id=cafeteria_id)
    return redirect('perfilCafeteria', id_cafeteria=cafeteria_id)

def historico(request):
    historico = Historico.objects.filter(user=request.user)
    return render(request, 'historico.html', {'historico': historico})

def remove_visit(request, visit_id):
    if request.method == 'POST':
        visit = Historico.objects.get(id=visit_id)
        visit.delete()
    return redirect('historico')

@login_required(login_url='login')
def ReservaCreateView(request, cafe_id):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.cafe = Estabelecimento.objects.get(id=cafe_id)
            reserva.cliente = request.user
            reserva.save()
            return redirect('reserva_list')
    else:
        form = ReservaForm()
    return render(request, 'reservaform.html', {'form': form})

@login_required(login_url='login')
def ReservaListView(request):
    reservas = Reserva.objects.filter(cliente=request.user).exclude(status='CA')
    return render(request, 'reservalist.html', {'reservas': reservas})

@login_required(login_url='login')
def ReservaUpdateView(request, reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)
    
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            reserva.status = Reserva.PENDENTE
            reserva.save()
            form.save()
            return redirect('reserva_list')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reservaupdate.html', {'form': form})
    
@login_required(login_url='login')

def ReservaCancelView(request, reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)
    if reserva.cliente == request.user and (reserva.status == Reserva.PENDENTE or reserva.status == Reserva.ACEITO):
        reserva.status = Reserva.CANCELADO
        reserva.save()
    return redirect('reserva_list')

@login_required(login_url='login')
def RecusarReservaView(request, reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)
    if reserva.cliente == request.user and reserva.status == Reserva.PENDENTE:
        reserva.status = Reserva.RECUSADO 
        reserva.save()
    return redirect('reserva_listar')

@login_required(login_url='login')
def AceitarReservaView(request, reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)
    if reserva.cliente == request.user and reserva.status == Reserva.PENDENTE:
        reserva.status = Reserva.ACEITO  
        reserva.save()
    return redirect('reserva_listar')

@login_required(login_url='login')
def listar_reservas(request):
    estabelecimento = Estabelecimento.objects.get(proprietario=request.user)
    reservas = Reserva.objects.filter(status=Reserva.PENDENTE, cafe=estabelecimento)
    return render(request, 'listarreservascafe.html', {'reservas': reservas,'possui_estabelecimento': request.user.possui_estabelecimento,'cafeteria':estabelecimento})

def solicitar_item(request, id_cafeteria):  # add id_cafeteria as an argument
    if request.method == 'POST':
        descricao = request.POST.get('descricao')

        cliente = request.user
        if Estabelecimento.objects.filter(id=id_cafeteria).exists():
            cafeteria = Estabelecimento.objects.get(id=id_cafeteria)
        lost_item = ItemEsquecido(cliente=cliente, cafeteria=cafeteria, descricao=descricao)
        lost_item.save()

        return redirect('historico')

    return render(request, 'solicitaritem.html')

def ver_solicitacoes(request):
    estabelecimento = Estabelecimento.objects.get(proprietario=request.user)
    solicitacoes = ItemEsquecido.objects.filter(cafeteria=request.user.cafeteria)
    return render(request, 'solicitacoes.html', {'solicitacoes': solicitacoes,'possui_estabelecimento': request.user.possui_estabelecimento,'cafeteria':estabelecimento})
def marcar_item_achado(request, item_id):
    item = get_object_or_404(ItemEsquecido, id=item_id, cafeteria=request.user.cafeteria)
    item.status = 'achado'
    item.save()
    return redirect('solicitacoes')

@login_required(login_url='login')
def marcar_item_nao_achado(request, item_id):
    item = get_object_or_404(ItemEsquecido, id=item_id, cafeteria=request.user.cafeteria)
    item.status = 'nao_achado'
    item.save()
    return redirect('solicitacoes')

@login_required(login_url='login')
def remover_requisicao(request, item_id):
    item = get_object_or_404(ItemEsquecido, id=item_id, cafeteria=request.user.cafeteria)
    item.delete()
    return redirect('solicitacoes')

@login_required(login_url='login')
def listar_requisicoes_cliente(request):
    requisicoes = ItemEsquecido.objects.filter(cliente=request.user)
    return render(request, 'minhassolicitacoes.html', {'requisicoes': requisicoes})