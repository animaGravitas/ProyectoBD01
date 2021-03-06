from django.http import HttpResponse
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
    personas = Persona.objects.all()
    data = {'personas':personas}
    return render(request, 'app_gestion/home.html', data)

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

def eliminar_personas(request):   
    if request.POST['txt_eliminar']:
        rut_recibido = request.POST['txt_eliminar']
        persona = Persona.objects.filter(rut=rut_recibido)
        if persona:
            per=Persona.objects.get(rut=rut_recibido)
            per.delete()
            mensaje = "Persona eliminada"
        else:
            mensaje = "Persona no eliminada; no existe" 
    else:
        mensaje = "Debe ingresar el rut para eliminar"    
    return HttpResponse(mensaje)        

     
    