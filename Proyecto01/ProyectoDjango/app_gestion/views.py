from django.shortcuts import redirect, render
from tomlkit import value
from app_gestion.models import Persona


def home(request):
    return render(request, 'app_gestion/home.html')

def gestion(request):
    return render(request, 'app_gestion/gestion.html') 

def listar(request):
    return render(request, 'app_gestion/listar.html')  

def eliminar(request):
    return render(request, 'app_gestion/eliminar.html')             
# Create your views here.

def listar_personas(request):
    datos = Persona.objects.all() 
    contexto = {'listarPersonas':datos} 
    return render(request, 'datos/listar.html', contexto)

def registrar_personas(request):
    rut = request.POST['txt_rut']
    nombre = request.POST['txt_nombre']
    appaterno = request.POST['txt_appaterno']
    apmaterno = request.POST['txt_apmaterno']
    edad = request.POST['nro_edad']
    vacuna = request.POST['slct_vacunas']
    #fecha = request.POST['dte.fecha']

    registro = Persona.objects.create(
        rut=rut, nombre=nombre, appaterno=appaterno, apmaterno=apmaterno,
        edad=edad, vacuna=vacuna)
    return redirect('/home/')
    