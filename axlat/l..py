# # import serial
# #
# # ser = serial.Serial(
# #     port='/dev/tty.usbserial-1410',\
# #     baudrate=9600,\
# #     parity=serial.PARITY_NONE,\
# #     stopbits=serial.STOPBITS_ONE,\
# #     bytesize=serial.EIGHTBITS,\
# #         timeout=0)
# #
# # print("connected to: " + ser.portstr)
# # count=1
# #
# # while True:
# #     for line in ser.read():
# #
# #         # print(str(count) + str(': ') + chr(line) )
# #         if chr(line) == 'w':
# #         count = count+1
# #
# # ser.close()
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # import serial
# # #
# # # # Tarozga bog'lanish uchun qurilma portini aniqlang
# # # serial_port = "/dev/tty.usbserial-1410"  # Unix tizimlarida
# # # # serial_port = "COM1"  # Windows tizimlarida
# # #
# # # # Taroz bilan bog'lanish uchun sozlashlar
# # # ser = serial.Serial(
# # #     port=serial_port,
# # #     baudrate=9600,
# # #     parity=serial.PARITY_NONE,
# # #     stopbits=serial.STOPBITS_ONE,
# # #     bytesize=serial.EIGHTBITS,
# # #     timeout=1
# # # )
# # #
# # # # Tarozdan olingan ma'lumotni o'qib chiqarish
# # # try:
# # #     while True:
# # #         line = ser.readline().decode().strip()
# # #         if line.startswith('W'):
# # #             weight_raw = int(line[1:])
# # #             kilograms = weight_raw // 1000
# # #             grams = weight_raw % 1000
# # #             print(f"{kilograms} kg {grams} g")
# # # except KeyboardInterrupt:
# # #     ser.close()
# #
# # import serial
# #
# # # Tarozga bog'lanish uchun qurilma portini aniqlang
# # serial_port = "/dev/tty.usbserial-1410"  # Unix tizimlarida
# # # serial_port = "COM1"  # Windows tizimlarida
# #
# # # Taroz bilan bog'lanish uchun sozlashlar
# # ser = serial.Serial(
# #     port=serial_port,
# #     baudrate=9600,
# #     parity=serial.PARITY_NONE,
# #     stopbits=serial.STOPBITS_ONE,
# #     bytesize=serial.EIGHTBITS,
# #     timeout=1
# # )
# #
# # def get_weight():
# #     line = ser.readline().decode().strip()
# #     if line.startswith('W'or "S"or "A"):
# #         weight_raw = int(line[1:])
# #         kilograms = weight_raw // 1000
# #         return kilograms
# #
# # # Tarozdan ma'lumot olish
# # try:
# #     while True:
# #         weight = get_weight()
# #         if weight is not None:
# #             print(f"{weight} kg")
# # except KeyboardInterrupt:
# #     ser.close()
# import serial
#
# # Seri port ayarları
# ser = serial.Serial('/dev/tty.usbserial-1410', 9600, timeout=1)  # Seri portu ve baud hızını ayarlayın
# while True:
#     def read_weight_from_scale():
#         ser.write(b'W\r\n')  # Taroziden kilo verisini almak için komut gönderin
#         response = ser.readline()  # Taroziden gelen yanıtı okuyun
#         weight = response.strip().decode('utf-8')  # Gelen veriyi düzenleyin
#         return weight
#
#     # Kilogram değerini oku ve ekrana yazdır
#     weight = read_weight_from_scale()
#     print(f"Kilogram: {weight}")
from django.shortcuts import render
from django.http import JsonResponse
import serial
import time

ser = serial.Serial('/dev/tty.usbserial-1410', 9600, timeout=0)

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

def continuous_weight(request):
    # if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
    while True:
        weight = read_weight_from_scale()
        print(f"Weight: {weight}")
        # response_data = {'weight': weight}
        # return JsonResponse(response_data)
        time.sleep(1)
        print(weight)