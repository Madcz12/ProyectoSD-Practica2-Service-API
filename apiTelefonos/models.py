from django.db import models

class Telefono(models.Model):
    tel_id = models.AutoField(primary_key=True)
    tel_nombre = models.CharField(max_length=150)

    class Meta:
        ordering = ['tel_id']  

class Repuesto(models.Model):
    rep_id = models.AutoField(primary_key=True)
    rep_nombre = models.CharField(max_length=150)    
    rep_tel = models.ForeignKey(Telefono, default=None, on_delete = models.CASCADE) # Llave foranea
    rep_precio = models.FloatField() 

    class Meta:
        ordering = ['rep_id']  

class Cliente(models.Model):
    cli_id = models.AutoField(primary_key=True)
    cli_nombre = models.CharField(max_length=150)
    cli_apellido = models.CharField(max_length=150)
    cli_cedula = models.CharField(max_length=150)
    cli_telefono = models.CharField(max_length=150)
    cli_direccion = models.CharField(max_length=250)
    cli_edad = models.IntegerField()

    class Meta:
        ordering = ['cli_id']

# class DetalleVenta(models.Model):
#     dven_id = models.AutoField(primary_key=True)
#     dven_rep = models.ManyToManyField(Repuesto)

#     class Meta:
#         ordering = ['dven_id']

class Venta(models.Model):
    ven_id = models.AutoField(primary_key=True)
    ven_cli = models.ForeignKey(Cliente, default=None, on_delete = models.CASCADE) # Llave foranea
    ven_monto = models.FloatField()     
    # ven_dven = models.ForeignKey(DetalleVenta, default=None, on_delete = models.CASCADE) # Llave foranea

    class Meta:
        ordering = ['ven_id']