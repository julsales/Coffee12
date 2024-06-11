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
	path('favoritarCafeteria/<int:id>/', views.FavoritarCafeteria, name='favoritarCafeteria'),
	path('desfavoritarCafeteria/<int:id>/', views.DesfavoritarCafeteria, name='desfavoritarCafeteria'),
	path('verCafeteriasFavoritas/',views.VerCafeteriasFavoritas,name='verCafeteriasFavoritas'),
	path('favoritos/',views.Favoritos,name='favoritos'),
	path('perfilCafeteria/<int:id_cafeteria>/', views.PerfilCafeteria, name='perfilCafeteria'),
	path('feedback/<int:id>/', views.feedback, name='feedback'),
	path('cafeteria/<int:id_cafeteria>/feedbacks/', views.VerFeedbacks, name='verFeedbacks'),
	path('add_to_historico/<int:cafeteria_id>/', views.add_to_historico, name='add_to_historico'),
	path('historico/', views.historico, name='historico'),
	path('remove_visit/<int:visit_id>/', views.remove_visit, name='remove_visit'),
	path('reserva/<int:cafe_id>/', views.ReservaCreateView, name='reserva_create'),
    path('reservas/', views.ReservaListView, name='reserva_list'),
    path('reserva/update/<int:reserva_id>/', views.ReservaUpdateView, name='reserva_update'),
	path('reserva/cancel/<int:reserva_id>/', views.ReservaCancelView, name='reserva_cancel'),
	path('reserva/<int:reserva_id>/recusar/', views.RecusarReservaView, name='reserva_recusar'),
    path('reserva/<int:reserva_id>/aceitar/', views.AceitarReservaView, name='reserva_aceitar'),
    path('reservas/listar/', views.listar_reservas, name='reserva_listar'),
	path('solicitaritem/<int:id_cafeteria>/', views.solicitar_item, name='solicitaritem'),
	path('solicitações/', views.ver_solicitacoes, name='solicitacoes'),
	path('marcar_item_achado/<int:item_id>/', views.marcar_item_achado, name='marcar_item_achado'),
    path('marcar_item_nao_achado/<int:item_id>/', views.marcar_item_nao_achado, name='marcar_item_nao_achado'),
    path('remover_requisicao/<int:item_id>/', views.remover_requisicao, name='remover_requisicao'),
    path('minhas_requisicoes/', views.listar_requisicoes_cliente, name='listar_requisicoes_cliente'),
    path('',views.Inicio,name='inicio'),
    
]
