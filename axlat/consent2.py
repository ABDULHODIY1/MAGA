import serial

# Seri port bağlantısını yapılandırma
ser = serial.Serial('/dev/tty.usbserial-1410', 9600)  # Seri port adı ve baud hızını belirtin (örneğin: COM1, 9600)

while True:
    # Seri porttan veri okuma
    data = ser.readline().decode().strip()  # Gelen veriyi okuyun ve gerekiyorsa işleyin

    # Gelen veriyi kullanarak istediğiniz hesaplamaları yapın
    tarozi_qiymati = float(data)
    qiymat_foyiz = (tarozi_qiymati - 1) * 100

    # Sonucu ekrana yazdırma
    print("Tarozi qiymati: {} gram".format(tarozi_qiymati))
    print("Qiymatning foyizi: {}%".format(qiymat_foyiz))

    # Gerekirse istediğiniz diğer işlemleri gerçekleştirin

# Seri port bağlantısını kapatma
ser.close()
