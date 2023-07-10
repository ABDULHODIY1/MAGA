# import serial
# import time
#
# ser = serial.Serial('/dev/tty.usbserial-1410', 9600, timeout=0)
#
# def read_weight_from_scale():
#     ser.write(b'W\r\n')
#     response = ser.readline()
#     response = response.decode('utf-8').strip()
#
#     if 'kg' in response:
#         weight = response.split(' ')[-2]
#     elif 'g' in response:
#         weight = float(response.split('   ')[-2]) / 1000
#     else:
#         weight = '0'
#
#     return weight
#
# def continuous_weight():
#     # if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
#         while True:
#             weight = read_weight_from_scale()
#             print(f"Weight: {weight}")
#             # response_data = {'weight': weight}
#             # return JsonResponse(response_data)
#             time.sleep(1)
#     # else:
#         # return render(request, 'temp.html')
import serial
import time

ser = serial.Serial('/dev/tty.usbserial-1420', 9600, timeout=0)

def read_weight_from_scale():
    ser.write(b'W\r\n')
    response = ser.readline()
    response = response.decode('utf-8').strip()

    if 'kg' in response:
        weight = response.split(' ')[-2]
    elif 'g' in response:
        weight = float(response.split(' ')[-2]) / 1000
    else:
        weight = '0'

    return weight

# @require_ajax
def continuous_weight():
    while True:
        weight = read_weight_from_scale()
        print(f"Weight: {weight}")
        # response_data = {'weight': weight}
        # return JsonResponse(response_data)
        time.sleep(1)

# def index(request):
#     # return render(request, 'template.html')

continuous_weight()
