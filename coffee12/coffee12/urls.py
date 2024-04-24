from django.contrib import admin
from django.urls import path
from coffee12app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', views.Homepage, name='homepage'),  # Rota para a página inicial
    path('signup/', views.SignupPage, name='signup'),  # Rota para a página de cadastro
    path('', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),
    path('signupCafe/',views.SignupCafePage,name='signupCafe')  # Rota para a página de login
    
]
