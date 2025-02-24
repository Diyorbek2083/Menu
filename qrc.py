import qrcode

def generate_qr_code(stol_raqami, wifi_ismi, wifi_paroli, fayl_nomi):
    """Stol uchun Wi-Fi va stol raqami kiritilgan QR kod yaratish"""
    data = f"WIFI:S:{wifi_ismi};T:WPA;P:{wifi_paroli};;\nStol: {stol_raqami}"
    qr = qrcode.make(data)  # QR kod yaratish
    qr.save(fayl_nomi)  # PNG formatida saqlash

# Foydalanish
stol_raqami = 1
wifi_ismi = "Kali"
wifi_paroli = "123456789000"
fayl_nomi = f"stol_{stol_raqami}.png"

generate_qr_code(stol_raqami, wifi_ismi, wifi_paroli, fayl_nomi)
print(f"{fayl_nomi} fayli yaratildi!")
