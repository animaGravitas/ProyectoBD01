from django.urls import path
from .views import home, gestion, listar, eliminar, listar_personas, registrar_personas, eliminar_personas

urlpatterns = [
    path('', home,name="home"),
    path('home/', home),
    path('gestion/', gestion,name="gestion"),
    path('listar/', listar,name="listar"),
    path('eliminar/', eliminar,name="eliminar"),
    path('listar_personas/', listar_personas,name="listar_personas"),
    path('registrar_personas/', registrar_personas,name="registrar_personas"),
    path('eliminar_personas/', eliminar_personas,name="eliminar_personas"),
]