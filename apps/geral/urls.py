from django.urls import path
from geral import views

app_name = 'geral'


urlpatterns = [
    path('nova-categoria/', views.nova_categoria, name='nova_categoria'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('logout/', views.logout_usuario, name='logout_usuario'),
    path('novo-usuario/', views.novo_usuario, name='novo_usuario'),
    path('relatorio/', views.relatorio, name='relatorio'),
    path('', views.principal, name='principal'),
]
