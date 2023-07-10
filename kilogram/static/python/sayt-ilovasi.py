import tkinter as tk
import requests
import serial

def read_weight_from_scale(scale_address, scale_port):
    ser = serial.Serial(scale_port, 9600, timeout=0)
    ser.write(b'W\r\n')
    response = ser.readline().decode('utf-8').strip()
    ser.close()

    if 'kg' in response:
        weight = response.split(' ')[-2]
    elif 'g' in response:
        weight = float(response.split('   ')[-2]) / 1000
    else:
        weight = '0'

    return weight

def send_weight_to_server(weight):
    server_url = "http://127.0.0.1:8000/Apis/scales-apis/"
    url = server_url + scale_address_entry.get() + "/"

    payload = {"weight": weight}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        result_label.config(text="Ma'lumotlar serverga muvaffaqiyatli yuborildi.")
    else:
        result_label.config(text="Ma'lumotlarni serverga yuborishda xatolik yuz berdi.")

def on_button_click():
    scale_port = scale_port_entry.get()
    weight = read_weight_from_scale(scale_address_entry.get(), scale_port)
    send_weight_to_server(weight)

window = tk.Tk()
window.title("Tarozdan ma'lumot olish")

scale_address_label = tk.Label(window, text="Taroz manzili:")
scale_address_label.pack()

scale_address_entry = tk.Entry(window)
scale_address_entry.pack()

scale_port_label = tk.Label(window, text="Tarozning porti:")
scale_port_label.pack()

scale_port_entry = tk.Entry(window)
scale_port_entry.pack()

button = tk.Button(window, text="Tarozdan ma'lumot olish", command=on_button_click)
button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
