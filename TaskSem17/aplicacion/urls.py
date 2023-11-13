from django.urls import path
from . import views

#Urls de la aplicacion
urlpatterns = [
path('vistaUrl', views.vista, name='vista'),
path('clienteUrl', views.cliente, name='cliente'),
path('ventasUrl', views.venta, name='ventas'),
path('empleadosUrl', views.empleado, name='empleado'),
path('areaUrl', views.area, name='area'),
]