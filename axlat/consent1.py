# # import serial
# #
# # port = "RS232"  # USB portning nomini to'g'ri o'rnating
# # baudrate = 9600
# #
# # weights = []  # Natijalarni saqlash uchun bo'sh ro'yxat
# # total_weight = 0  # Umumiy og'irlik
# #
# # with serial.Serial(port, baudrate) as ser:
# #     while True:
# #         if ser.in_waiting > 0:
# #             data = ser.readline()
# #             try:
# #                 weight = float(data.decode("ASCII").strip())
# #                 weights.append(weight)
# #                 total_weight += weight
# #                 print(f"Current Weight: {weight:.3f}kg")
# #                 print(f"Total Weight: {total_weight:.3f}kg")
# #                 print(f"Weight List: {weights}")
# #             except (UnicodeDecodeError, ValueError):
# #                 pass
#
# import serial
# import time
#
# port = "/dev/tty.usbserial-1410"  # USB portning nomini to'g'ri o'rnating
# baudrate = 9600
#
# with serial.Serial(port, baudrate) as ser:
#     while True:
#         try:
#             # Data oluvchi davomiy tsikl
#             data = ser.readline().decode("ASCII").strip()  # Ma'lumotni o'qish
#             print(data)  # Ma'lumotni chiqarish
#             time.sleep(1)  # 1 sekund kutish
#         except UnicodeDecodeError:
#             pass
#
import serial

port = "/dev/tty.usbserial-1410"  # USB portning nomini to'g'ri o'rnating
baudrate = 9600

# Tarozingizning boshlang'ich og'irlik qiymati
initial_weight = 0

with serial.Serial(port, baudrate) as ser:
    current_weight = initial_weight  # Joriy og'irlikni saqlash uchun o'zgaruvchi
    while True:
        try:
            data = ser.readline().decode("ASCII").strip()  # Ma'lumotni o'qish
            weight_change = float(data)  # O'girlik o'zgarishini hisoblash
            current_weight += weight_change  # Joriy og'irlikni yangilash
            print(f"Current Weight: {current_weight:.3f}kg")
        except (UnicodeDecodeError, ValueError):
            pass
