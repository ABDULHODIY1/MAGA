from django.http import JsonResponse
import serial.tools.list_ports

def get_usb_ports(request):
    usb_ports = list(serial.tools.list_ports.comports())
    usb_devices = []

    for port in usb_ports:
        device_info = {
            'device_name': port.device,
            'device_description': port.description,
            'device_manufacturer': port.manufacturer
        }
        usb_devices.append(device_info)

    response_data = {
        'status': 'success',
        'devices': usb_devices
    }
    return JsonResponse(response_data)
