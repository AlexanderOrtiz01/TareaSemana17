from django.db import models

#Tabla cliente
class cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    dui = models.IntegerField()
#Tabla Area
class area(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_Area = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=300)

#Tabla empleado
class empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    Edad = models.IntegerField()
    areaId = models.ForeignKey(area, on_delete=models.CASCADE)

#Tabla venta
class venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_venta = models.DateTimeField()
    monto = models.DecimalField(max_digits=9, decimal_places=2)
    clienteId = models.ForeignKey(cliente, on_delete=models.CASCADE)
    empleadoId = models.ForeignKey(empleado, on_delete=models.CASCADE)