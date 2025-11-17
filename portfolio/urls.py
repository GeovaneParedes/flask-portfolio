from django.urls import path
from . import views

urlpatterns = [
    # Mapeia a URL raiz ('') para a função index da view
    path('', views.index, name='index'), 
]
