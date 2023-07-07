import speech_recognition as sr
import pyttsx3
import os
import keyboard
import configparser
import time
from tkinter import *

key1 , key2 = "F9" , "กด Start "
config_file = "config.ini"

config = configparser.ConfigParser()
config.read(config_file)

if not os.path.isfile(config_file):
    # สร้างไฟล์ config.ini หากยังไม่มี
    config['program'] = {
        'discord': 'Discord',
        'program1': '',
        'program2': '',
        'program3': '',
        'program4': '',
        'program5': ''
    }
    with open(config_file, 'w') as configfile:
        config.write(configfile)

print( key2 , key1)
# Create a speech recognizer
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function for text-to-speech output
def speak(text):
    engine.say(text)
    engine.runAndWait()

running = True  # Flag to indicate if the program is running
def start():
    while running:
        if keyboard.is_pressed(key1):
            print("start")
            with sr.Microphone() as source:
                audio = r.listen(source)

                try:
                    text = r.recognize_google(audio, language='th')
                    print("Recognized Text:", text)  # Added print statement

                    if "เปิด Powerpoint" in text:
                        os.system('start POWERPNT.EXE')

                    if "เปิด Word" in text:
                        os.system("start WINWORD.EXE")

                    if "เปิด YouTube" in text:
                        os.system("start https://youtube.com")

                    if "เปิด discord" in text or "เปิดดิสคอร์ด" in text:
                        discord = config.get("program","discord")
                        os.system(f'start {discord}')

                    if "เปิด Excel" in text:
                        os.system("start EXCEL.EXE")

                    if "ปิดแชท gpt" in text:
                        os.system("start https://chat.openai.com/")

                    if "เปิด Facebook" in text:
                        os.system("start https://www.facebook.com/")

                    if "ลบไฟล์ขยะ" in text:
                        os.system("rd %temp% /s /q")

                    if "ปิดโปรแรกม" in text:
                        exit()

                    if "เปิด 1" in text:
                        program1 = config.get("program", "program1")
                        os.system(f"start {program1}")

                    if "เปิด 2" in text:
                        program2 = config.get("program", "program2")
                        os.system(f"start {program2}")

                    if "เปิด 3" in text:
                        program3 = config.get("program", "program3")
                        os.system(f"start {program3}")

                    if "เปิด 4" in text:
                        program4 = config.get("program", "program4")
                        os.system(f"start {program4}")

                    if "เปิด 5" in text:
                        program5 = config.get("program", "program5")
                        os.system(f"start {program5}")

                    if "เปิดเว็บ" in text:
                        
                        with sr.Microphone() as source:
                            print("https อะไร")
                            time.sleep(1)
                            audio = r.listen(source)
                            
                            r1 = sr.Recognizer()
                            text1 = r1.recognize_google(audio, language='th')
                            
                            os.system(f"start https://{text1}")
                            print("Recognized Text:", text1)

                except sr.UnknownValueError:
                    print("ไม่สามารถรับรู้เสียงได้")
                except sr.RequestError as e:
                    print("พบข้อผิดพลาดจากการร้องขอ:", str(e))

start()
