from django.http import Http404, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from apiTelefonos import serializers
from apiTelefonos.models import Telefono, Repuesto, Cliente, Venta
from apiTelefonos.serializers import ClienteSerializer, RepuestoSerializer, TelefonoSerializer, VentaSerializer
import json

from rest_framework.pagination import PageNumberPagination

class TestimoniosSetPagination(PageNumberPagination):
    page_size = 5

# Telefonos
@csrf_exempt
@api_view(['GET', 'POST']) # Trae lista de resultados y por post puede cargar varios "Repuestos"
def telefonos_list(request):    

    if request.method == 'GET':
        telefonos = Telefono.objects.all()                
        paginator = PageNumberPagination()
        results = paginator.paginate_queryset(telefonos, request)
        if results is not None:
            serializer = TelefonoSerializer(results, many=True)
            return paginator.get_paginated_response(serializer.data) 

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TelefonoSerializer(data=data)
        if serializer.is_valid():                        
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)   

@csrf_exempt
@api_view(['GET', 'PATCH', 'DELETE']) # Patch to edit
def telefono_detail(request, pk):

    try:
        telefono = Telefono.objects.get(pk=pk)
    except Telefono.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TelefonoSerializer(telefono)
        return JsonResponse(serializer.data)

    if request.method == 'PATCH':
        # Data en json del body del query
        data = JSONParser().parse(request) 

        telefono_edit = telefono
        telefono_edit.tel_nombre = data['tel_nombre']
        telefono.save()

        # Si se guarda efectivamente manda status 200 = OK
        return HttpResponse(status=200)

    elif request.method == 'DELETE':
        telefono.delete()
        return HttpResponse(status=204)

# -----------------------------------------------------------------

# Repuestos
@csrf_exempt
@api_view(['GET', 'POST']) # Trae lista de resultados y por post puede cargar varios "Repuestos"
def repuestos_list(request):    

    if request.method == 'GET':
        respuestos = Repuesto.objects.all()                
        paginator = PageNumberPagination()
        results = paginator.paginate_queryset(respuestos, request)
        if results is not None:
            serializer = RepuestoSerializer(results, many=True)
            return paginator.get_paginated_response(serializer.data) 

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RepuestoSerializer(data=data)
        if serializer.is_valid():                        
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)   

@csrf_exempt
@api_view(['GET', 'PATCH', 'DELETE']) # Patch to edit
def repuesto_detail(request, pk):

    try:
        repuesto = Repuesto.objects.get(pk=pk)
    except Repuesto.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RepuestoSerializer(repuesto)
        return JsonResponse(serializer.data)

    if request.method == 'PATCH':
        # Data en json del body del query
        data = JSONParser().parse(request) 

        repuesto_edit = repuesto
        repuesto_edit.rep_nombre = data['rep_nombre']
        repuesto_edit.rep_tel = data['rep_tel']
        repuesto_edit.rep_precio = data['rep_precio']
        repuesto_edit.save()

        # Si se guarda efectivamente manda status 200 = OK
        return HttpResponse(status=200)

    elif request.method == 'DELETE':
        repuesto.delete()
        return HttpResponse(status=204)

# -----------------------------------------------------------------

# Clientes
@csrf_exempt
@api_view(['GET', 'POST']) 
def clientes_list(request):    

    if request.method == 'GET':
        clientes = Cliente.objects.all()                
        paginator = PageNumberPagination()
        results = paginator.paginate_queryset(clientes, request)
        if results is not None:
            serializer = ClienteSerializer(results, many=True)
            return paginator.get_paginated_response(serializer.data) 

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClienteSerializer(data=data)
        if serializer.is_valid():                        
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)   

@csrf_exempt
@api_view(['GET', 'PATCH', 'DELETE']) # Patch to edit
def cliente_detail(request, pk):

    try:
        cliente = Cliente.objects.get(pk=pk)
    except Cliente.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ClienteSerializer(cliente)
        return JsonResponse(serializer.data)

    if request.method == 'PATCH':
        # Data en json del body del query
        data = JSONParser().parse(request) 

        cliente_edit = cliente        
        cliente_edit.cli_nombre = data['cli_nombre']
        cliente_edit.cli_apellido = data['cli_apellido']
        cliente_edit.cli_cedula = data['cli_cedula']
        cliente_edit.cli_telefono = data['cli_telefono']
        cliente_edit.cli_direccion = data['cli_direccion']
        cliente_edit.save()

        # Si se guarda efectivamente manda status 200 = OK
        return HttpResponse(status=200)

    elif request.method == 'DELETE':
        cliente.delete()
        return HttpResponse(status=204)

# -----------------------------------------------------------------

# # Detalle Venta
# @csrf_exempt
# @api_view(['GET', 'POST']) 
# def detalle_venta_list(request):    

#     if request.method == 'GET':
#         detalle_ventas = DetalleVenta.objects.all()                
#         paginator = PageNumberPagination()
#         results = paginator.paginate_queryset(detalle_ventas, request)
#         if results is not None:
#             serializer = DetalleVentaSerializer(results, many=True)
#             return paginator.get_paginated_response(serializer.data) 

#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = DetalleVentaSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)   

# @csrf_exempt
# @api_view(['GET', 'PATCH', 'DELETE'])
# def detalle_venta_detail(request, pk):

#     try:
#         detalle_venta = DetalleVenta.objects.get(pk=pk)
#     except Venta.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = DetalleVentaSerializer(detalle_venta)
#         return JsonResponse(serializer.data)

#     if request.method == 'PATCH':
#         # Data en json del body del query
#         data = JSONParser().parse(request) 

#         detalle_venta_edit = detalle_venta                
#         detalle_venta_edit.dven_rep = data['dven_rep']        
#         detalle_venta_edit.save()

#         # Si se guarda efectivamente manda status 200 = OK
#         return HttpResponse(status=200)

#     elif request.method == 'DELETE':
#         detalle_venta.delete()
#         return HttpResponse(status=204)

# # -----------------------------------------------------------------

# Venta
@csrf_exempt
@api_view(['GET', 'POST']) # Trae lista de resultados y por post puede cargar varios "Repuestos"
def ventas_list(request):    

    if request.method == 'GET':
        ventas = Venta.objects.all()                
        paginator = PageNumberPagination()
        results = paginator.paginate_queryset(ventas, request)
        if results is not None:
            serializer = VentaSerializer(results, many=True)
            return paginator.get_paginated_response(serializer.data) 

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VentaSerializer(data=data)
        if serializer.is_valid():                        
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)   

@csrf_exempt
@api_view(['GET', 'PATCH', 'DELETE']) # Patch to edit
def ventas_detail(request, pk):

    try:
        venta = Venta.objects.get(pk=pk)
    except Venta.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VentaSerializer(venta)
        return JsonResponse(serializer.data)

    if request.method == 'PATCH':
        # Data en json del body del query
        data = JSONParser().parse(request) 

        venta_edit = venta                
        venta_edit.ven_cli = data['ven_cli']
        venta_edit.ven_monto = data['ven_monto']        
        venta_edit.save()

        # Si se guarda efectivamente manda status 200 = OK
        return HttpResponse(status=200)

    elif request.method == 'DELETE':
        venta.delete()
        return HttpResponse(status=204)

# -----------------------------------------------------------------