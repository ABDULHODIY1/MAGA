# import webbrowser
# import os
#
#
# def natijani_korsat(url):
#
#
#     webbrowser.open(url)
#
# manzil = input("Python faylning manzilini kiriting: ")
#
# try:
#     with open(manzil, 'r') as file:
#         # Faylni ishga tushurish bilan bog'liq barcha loyihani bajarishingiz mumkin
#         # Misol uchun, faylni o'qib, ma'lumotlar bilan amal bajarish, natijani chiqarish, kabi
#         # Bu joyda sizning ustozlik dasturida kerak bo'lgan qo'shimcha kodlarni qo'shishingiz mumkin
#
#         # Natijani chiqarish
#         html = """
#         <html>
#         <head></head>
#         <body>
#             <p>Natija: 123</p>
#         </body>
#         </html>
#         """
#         temp_file = 'Templates/temp.html'
#         with open(temp_file, 'w') as temp:
#             temp.write(html)
#         natijani_korsat('file: // ' + os.path.realpath(temp_file))
#
# except FileNotFoundError:
#     print("Fayl topilmadi!")
#
# # Kod yuklanmagan natija chiqarish
# print("Natija ozgarganida pastki qismi: 404 Not Found")
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for port in ports:
    print(port.device)
