from msilib.schema import ListView
from re import template
from winreg import REG_RESOURCE_REQUIREMENTS_LIST
from django.http import HttpResponse
from django.shortcuts import render
from Libreria.forms import LectorFormulario, PrestamoFormulario, LibroFormulario, UserRegisterForm, AvatarFormulario
from Libreria.models import Lector, Prestamo, Libro, Avatar
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


#Registrar usuario

def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username=form.cleaned_data['username']
            form.save()

            return render(request, "Libreria/inicio.html", {'mensaje':"Usuario Creado"})
    else:

        form = UserRegisterForm()

    return render(request, "Libreria/registro.html", {'form':form})


#login

def login_request(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')    

            user=authenticate(username=usuario, password=contra)

            if user:

                login(request, user)

                return render(request, "Libreria/inicio.html", {'mensaje':f"Bienvenido {user}"})
        
        else:

            return render(request, "Libreria/inicio.html", {'mensaje': "Error. Datos incorrectos"})       

    else:

        form = AuthenticationForm()   

    return render(request, "Libreria/login.html", {'form':form})


@login_required
def lector(request):
    
    if request.method == 'POST':

        miFormulario= LectorFormulario(request.POST)

        if miFormulario.is_valid():
            
            info= miFormulario.cleaned_data

            lector= Lector(nombre= info['nombre'], apellido= info['apellido'], telefono= info['telefono'], libroEnPrestamo= info['libroEnPrestamo'])

            lector.save()

            return render(request, 'Libreria/inicio.html')

    else:

        miFormulario= LectorFormulario()    


    return render(request,'Libreria/lector.html', {'miFormulario':miFormulario})
@login_required
def prestamo(request):
    
    if request.method == 'POST':

        miFormulario= PrestamoFormulario(request.POST)

        if miFormulario.is_valid():
            
            info= miFormulario.cleaned_data

            prestamo= Prestamo(lector= info['lector'], libro= info['libro'], fechaDePrestamo= info['fechaDePrestamo'], devuelto= info['devuelto'])

            prestamo.save()

            return render(request, 'Libreria/inicio.html')

    else:

        miFormulario= PrestamoFormulario()    


    return render(request,'Libreria/prestamo.html', {'miFormulario':miFormulario})
@login_required
def libro(request):

    if request.method == 'POST':

        miFormulario= LibroFormulario(request.POST)

        if miFormulario.is_valid():
            
            info= miFormulario.cleaned_data

            libro= Libro(nombre= info['nombre'], enPrestamo= info['enPrestamo'])

            libro.save()

            return render(request, 'Libreria/inicio.html')

    else:

        miFormulario= LibroFormulario()
    

    return render(request,'Libreria/libro.html', {'miFormulario':miFormulario})


def AcercaDeMi(request):
    

    return render(request,'Libreria/AcercaDeMi.html')

def inicio(request):
    

    return render(request,'Libreria/inicio.html')

@login_required

def buscarPrestamo(request):

    return render(request, 'Libreria/buscarPrestamo.html')

def buscar(request):
    if request.GET["lector"]:
       

        lector= request.GET["lector"]
        prestamos= Prestamo.objects.filter(lector__icontains=lector)

        return render(request, 'Libreria/resultadosBusqueda.html', {"prestamos":prestamos, "lector":lector})
    else:

        respuesta= "No ingresaste datos" 

    return HttpResponse(respuesta)

#Vista para subir avatares
@login_required
def agregarImagen(request):

    if request.method == 'POST':

       miFormulario = AvatarFormulario(request.POST, request.FILES) 

       if miFormulario.is_valid():

           u = User.objects.get(username=request.user)

           avatar = Avatar(user = u, imagen= miFormulario.cleaned_data['imagen'])

           avatar.save()

           return render(request,'Libreria/inicio.html')
    
    else:

        miFormulario = AvatarFormulario()

        return render(request, "Libreria/agregarImagen.html", {'miFormulario': miFormulario})







class LibroList(LoginRequiredMixin ,ListView):
    
    model = Libro
    template_name = "Libreria/ListaLibros.html"

class LibroDetalle(LoginRequiredMixin ,DeleteView):
    
    model = Libro
    template_name = "Libreria/LibroDetalles.html"

class LibroCreate(LoginRequiredMixin ,CreateView):
    
    model = Libro
    success_url  = "/Libreria/libro/lista"
    fields = ['nombre','enPrestamo']

class LibroUpdate(LoginRequiredMixin, UpdateView):
    
    model = Libro
    success_url  = "/Libreria/libro/lista"
    fields = ['nombre','enPrestamo']

class LibroDelete(LoginRequiredMixin, DeleteView):
    
    model = Libro
    success_url = "/Libreria/libro/lista"




class LectorList(LoginRequiredMixin, ListView):
    
    model = Lector
    template_name = "Libreria/ListaLectores.html"

class LectorDetalle(LoginRequiredMixin, DeleteView):
    
    model = Lector
    template_name = "Libreria/LectorDetalles.html"

class LectorCreate(LoginRequiredMixin, CreateView):
    
    model = Lector
    success_url  = "/Libreria/Lector/lista"
    fields = ['nombre','apellido','telefono','libroEnPrestamo']

class LectorUpdate(LoginRequiredMixin, UpdateView):
    
    model = Lector
    success_url  = "/Libreria/lector/lista"
    fields = ['nombre','apellido','telefono','libroEnPrestamo']

class LectorDelete(LoginRequiredMixin, DeleteView):
    
    model = Lector
    success_url = "/Libreria/lector/lista"





class PrestamoList(LoginRequiredMixin, ListView):
    
    model = Prestamo
    template_name = "Libreria/ListaPrestamos.html"

class PrestamoDetalle(LoginRequiredMixin, DeleteView):
    
    model = Prestamo
    template_name = "Libreria/PrestamoDetalle.html"

class PrestamoCreate(LoginRequiredMixin, CreateView):
    
    model = Prestamo
    success_url  = "/Libreria/prestamo/lista"
    fields = ['lector','libro','fechaDePrestamo','devuelto']


class PrestamoDelete(LoginRequiredMixin, DeleteView):
    
    model = Prestamo
    success_url = "/Libreria/prestamo/lista"



  



