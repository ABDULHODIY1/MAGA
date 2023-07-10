from django.urls import path
from . import views

urlpatterns = [
    path('api/usb-ports/', views.get_usb_ports, name='get_usb_ports'),
]
