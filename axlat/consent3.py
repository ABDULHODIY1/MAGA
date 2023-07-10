# import serial
#
# ser = serial.Serial(
#     port='/dev/tty.usbserial-1410',
#     baudrate=9600,
#     parity=serial.PARITY_NONE,
#     stopbits=serial.STOPBITS_ONE,
#     bytesize=serial.EIGHTBITS,
#     timeout=None,
#     rx_buffer_size=4096  # Misol uchun 4096 bayt
# )
#
#
# print("connected to: " + ser.portstr)
# count = 2
#
# while True:
#     line = ser.readline().decode().strip()
#
#     if line.startswith('W'):  # W berilgan takrorlanuvchi qism
#         weight = int(line[1:]) / 1000  # gramdan kilogramgacha o'tkazamiz
#         print(str(count) + ': ' + str(weight) + ' kg')
#         count += 1
#
# ser.close()
import serial
import time

ser = serial.Serial(
    port='/dev/tty.usbserial-1410',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=None
)

print("connected to: " + ser.portstr)

def read_weight():
    line = ser.readline().decode().strip()
    if line.startswith('W'):  # W berilgan takrorlanuvchi qism
        weight_raw = int(line[1:])  # gram cinsidan olingan ma'lumot
        kilograms = weight_raw // 1000
        grams = weight_raw % 1000
        print(str(kilograms) + ' kg ' + str(grams) + ' g')

while True:
    if ser.in_waiting > 0:
        read_weight()
    time.sleep(0.1)  # 0.1 sekund kutamiz

ser.close()
