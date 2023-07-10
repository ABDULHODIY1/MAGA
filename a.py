from django.http import HttpResponse
from django.views.decorators.http import condition
import serial
import time

ser = serial.Serial('/dev/tty.usbserial-1420', 9600, timeout=0)
last_modified = None


def read_weight_from_scale():
    ser.write(b'W\r\n')
    response = ser.readline()
    response = response.decode('utf-8').strip()

    if 'kg' in response:
        weight = response.split(' ')[-2]
    elif 'g' in response:
        weight = float(response.split('   ')[-2]) / 1000
    else:
        weight = '0'

    return weight


def get_weight():
    global last_modified
    weight = read_weight_from_scale()
    last_modified = time.time()
    return HttpResponse(f"Weight: {weight}")


def weight_etag(request):
    global last_modified
    return str(last_modified) if last_modified else None


# @condition(etag_func=weight_etag)
def continuous_weight():
    def stream_response():
        while True:
            weight = read_weight_from_scale()
            print( f"Weight: {weight}\n")
            time.sleep(0.1)

    response = HttpResponse(stream_response(), content_type='text/plain')
    response['Cache-Control'] = 'no-cache'
    return response
