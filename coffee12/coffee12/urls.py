from django.contrib import admin
from django.urls import path
from coffee12app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', views.Homepage, name='homepage'),
    path('homepagecafe/', views.HomepageCafe, name='homepagecafe'),  # Rota para a página inicial
    path('signup/', views.SignupPage, name='signup'),  # Rota para a página de cadastro
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),
    path('signupCafe/',views.SignupCafePage,name='signupCafe'),  # Rota para a página de login
    path('cadastrarEstabelecimento/',views.CadastrarEstabelecimento,name='cadastrarEstabelecimento'),
    path('cadastrarPrato/',views.CadastrarPrato,name='cadastrarPrato'),
    path('editarEstabelecimento/',views.EditarEstabelecimento,name='editarEstabelecimento'),
    path('excluirEstabelecimento/',views.ExcluirEstabelecimento,name='excluirEstabelecimento'),
    path('excluirPrato/',views.ExcluirPrato,name='excluirPrato'),
	path('favoritarCafeteria/',views.FavoritarCafeteria,name='favoritarCafeteria'),
	path('desfavoritarCafeteria/',views.DesfavoritarCafeteria,name='desfavoritarCafeteria'),
	path('verCafeteriasFavoritas/',views.VerCafeteriasFavoritas,name='verCafeteriasFavoritas'),
    path('',views.Inicio,name='inicio'),
    
]
