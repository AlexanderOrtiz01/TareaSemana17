from django.shortcuts import render
from .models import cliente as clienteModels
from .models import venta  as ventaModels
from .models import empleado as empleadoModels
from .models import area as areaModels

# Create your views here.

#Todas y cada una de las vistas utilizadas
def vista(request):
    return render(request, "pagina.html")

def cliente(request):
    clientesObj = clienteModels.objects.all()
    return render(request, "clientes.html",{"clienteT":clientesObj})

def venta(request):
    ventasObj = ventaModels.objects.all()
    return render(request, "ventas.html",{"ventaT":ventasObj})

def empleado(request):
    empleadoObj = empleadoModels.objects.all()
    return render(request, "empleados.html",{"empleadoT":empleadoObj})

def area(request):
    areaObj = areaModels.objects.all()
    return render(request, "area.html",{"areaT":areaObj})
