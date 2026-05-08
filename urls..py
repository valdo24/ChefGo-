from django.urls import path
from . import views  # Importa tus vistas

urlpatterns = [
    # Si quieres que sea la página principal, el primer argumento queda vacío ''
    path('', views.feed_view, name='uno'), 
]