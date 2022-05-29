import imp
from django.urls import path
from Libreria import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('lector/', views.lector,name='Lectores'),
    path('prestamo/', views.prestamo, name= 'Prestamos'),
    path('libro/', views.libro, name= 'Libros'),
    path('', views.inicio, name= 'Inicio'),
    path('AcercaDeMi/', views.AcercaDeMi, name= 'AcercaDeMi'),
    path('buscarPrestamo/', views.buscarPrestamo, name= 'BuscarPrestamo'),
    path('buscar/', views.buscar),
   
    path('libro/lista', views.LibroList.as_view(), name="ListLibros"),
    path(r'^(?P<pk>\d+)$1', views.LibroDetalle.as_view(), name= 'Detail'),
    path(r'^nuevo$1', views.LibroCreate.as_view(), name= 'New'),
    path(r'^editar/(?P<pk>\d+)$1', views.LibroUpdate.as_view(), name= 'Edit'),
    path(r'^borrar/(?P<pk>\d+)$1', views.LibroDelete.as_view(), name= 'Delete'),

    path('lector/lista', views.LectorList.as_view(), name="ListLector"),
    path(r'^(?P<pk>\d+)$2', views.LectorDetalle.as_view(), name= 'LectorDetail'),
    path(r'^nuevo$2', views.LectorCreate.as_view(), name= 'LectorNew'),
    path(r'^editar/(?P<pk>\d+)$2', views.LectorUpdate.as_view(), name= 'LectorEdit'),
    path(r'^borrar/(?P<pk>\d+)$2', views.LectorDelete.as_view(), name= 'LectorDelete'),
    
    path('prestamo/lista', views.PrestamoList.as_view(), name="ListPrestamo"),
    path(r'^(?P<pk>\d+)$3', views.PrestamoDetalle.as_view(), name= 'PrestamoDetail'),
    path(r'^nuevo$3', views.PrestamoCreate.as_view(), name= 'PrestamoNew'),
    path(r'^borrar/(?P<pk>\d+)$3', views.PrestamoDelete.as_view(), name= 'PrestamoDelete'),

    path('login', views.login_request, name = 'Login'),
    path('logout', LogoutView.as_view(template_name='Libreria/logout.html'), name='logout'),
    path('register', views.register, name = 'register'),

    path('agregarImagen', views.agregarImagen, name= 'SubirAvatar')

]