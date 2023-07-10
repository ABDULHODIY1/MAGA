import serial

ser = serial.Serial(
    port='/dev/tty.usbserial-1410',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0
)

print("connected to: " + ser.portstr)
count = 1

while True:
    line = ser.readline().decode().strip()
    if line.startswith("S"):
        weight_raw = int(line[1:])
        kilograms = weight_raw // 1000
        grams = weight_raw % 1000
        print(str(count) + ': ' + str(kilograms) + ' kg ' + str(grams) + ' g')
        count += 1

ser.close()
# import numpy as np
# import time
#
# from serial_weighing_scale import SerialWeighingScale
#
# serial_port = "/dev/tty.usbserial-1410"  # for Unix systems. "COM1" on Windows systems
# scale = SerialWeighingScale(port=serial_port)
#
# while not scale.scale_is_ready():
#     time.sleep(.1)
#
# # Perform standard operations
# scale.tare_scale()  # Tare scale
# scale.read_weight()  # Take single measurement
# scale.read_weight_repeated(n_readings=5)  # Get n readings
# scale.read_weight_reliable(n_readings=5, measure=np.mean)  # Get statistic of n readings

#
import serial

# Tarozga bog'lanish uchun qurilma portini aniqlang
serial_port = "/dev/tty.usbserial-1410"  # Unix tizimlarida
# serial_port = "COM1"  # Windows tizimlarida

# Taroz bilan bog'lanish uchun sozlashlar
ser = serial.Serial(
    port=serial_port,
    baudrate=1119600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

# Tarozdan olingan ma'lumotni o'qib chiqarish
try:
    while True:
        line = ser.readline().decode().strip()
        print(line)
except KeyboardInterrupt:
    ser.close()
print(line)
