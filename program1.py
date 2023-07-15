import requests , speech_recognition as sr , os , configparser , threading , keyboard
from gtts import gTTS
from playsound import playsound
from tkinter import *
from io import BytesIO
from PIL import Image

print("กำลังโหลดอยู่")
# URL ของไฟล์โค้ดที่ต้องการดาวน์โหลด
url = "https://raw.githubusercontent.com/knhdsa/voice_pro_up/main/program0.py"
print("โหลดเสร็จ")

def download_icon(url, save_path):
    response = requests.get(url)
    icon_data = response.content
    with open(save_path, 'wb') as f:
        f.write(icon_data)

download_icon("https://raw.githubusercontent.com/knhdsa/icon-Knhdsa/main/channels4_profile.ico","icon.ico")

# ดาวน์โหลดโค้ดจาก URL
response = requests.get(url)
code = response.text

# รันโค้ดที่ดาวน์โหลดมา
exec(code)
