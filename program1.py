import requests
import speech_recognition as sr

print("กำลังโหลดอยู่")
# URL ของไฟล์โค้ดที่ต้องการดาวน์โหลด
url = "https://raw.githubusercontent.com/knhdsa/voice_pro_up/main/program0.py"
print("โหลดเสร็จ")
# ดาวน์โหลดโค้ดจาก URL
response = requests.get(url)
code = response.text

# รันโค้ดที่ดาวน์โหลดมา
exec(code)
