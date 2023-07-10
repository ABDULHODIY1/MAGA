import usb.core
import usb.backend

# Backendni tekshirish
backend = usb.backend.get_backend()

# USB qurilmasini izlaymiz
device = usb.core.find(backend=backend)

# USB qurilmasini aniqlaymiz
if device is None:
    raise ValueError("Qurilmangiz topilmadi!")

# USB qurilmasining ma'lumotlarini olish
data = device.read(0x81, 64)  # 64 baytlik ma'lumotni o'qish uchun

# Olingan ma'lumotni ekranga chiqaramiz
print(data)
