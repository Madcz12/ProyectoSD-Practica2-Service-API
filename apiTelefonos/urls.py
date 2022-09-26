from django.urls import path
from apiTelefonos import views

urlpatterns = [
    # Telefonos
    path('telefonos/', views.telefonos_list),
    path('telefonos_detail/<int:pk>/', views.telefono_detail),

    # Repuestos
    path('repuestos/', views.repuestos_list),
    path('repuestos_detail/<int:pk>/', views.repuesto_detail),

    # Clientes
    path('clientes/', views.clientes_list),
    path('clientes_detail/<int:pk>/', views.cliente_detail),

    # # DetalleVentas
    # path('detalle_ventas/', views.detalle_venta_list),
    # path('detalle_ventas_detail/<int:pk>/', views.detalle_venta_detail),

    # Ventas
    path('ventas/', views.ventas_list),
    path('ventas_detail/<int:pk>/', views.ventas_detail),
]
