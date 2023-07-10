from flask import Flask, jsonify
import serial
import time

app = Flask(__name__)
ser = serial.Serial('/dev/tty.usbserial-1410', 9600, timeout=0)

def tarozidan_ogirlik_olish():
    ser.write(b'W\r\n')
    javob = ser.readline()
    javob = javob.decode('utf-8').strip()

    if 'kg' in javob:
        ogirlik = javob.split(' ')[-2]
    elif 'g' in javob:
        ogirlik = float(javob.split(' ')[-2]) / 1000
    else:
        ogirlik = 0

    return ogirlik

@app.route('/ogirlik_olish')
def ogirlik_olish():
    ogirlik = tarozidan_ogirlik_olish()
    return jsonify({'ogirlik': ogirlik})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
