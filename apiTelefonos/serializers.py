from apiTelefonos.models import Cliente, Telefono, Repuesto, Venta
from rest_framework import serializers

class TelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefono
        fields = [ 
            'tel_id',
            'tel_nombre'
        ]

class RepuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repuesto
        fields = [ 
            'rep_id',
            'rep_nombre',
            'rep_tel',
            'rep_precio'
        ]

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'cli_id',
            'cli_nombre',
            'cli_apellido',
            'cli_cedula',
            'cli_telefono',
            'cli_direccion',
            'cli_edad'
        ]

# class DetalleVentaSerializer(serializers.ModelSerializer):
#     repuesto = RepuestoSerializer(read_only=True, many=True)

#     class Meta:
#         model = DetalleVenta
#         fields = ['repuesto']

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = [
            'ven_id',
            'ven_cli',
            'ven_monto'            
        ]