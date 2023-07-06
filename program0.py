import speech_recognition as sr
import pyttsx3
import os
import keyboard
from tkinter import *

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
        if keyboard.is_pressed("ctrl+shift+f9"):
            print("start")
            with sr.Microphone() as source:
                audio = r.listen(source)


def run():
    while running:
        if keyboard.is_pressed("ctrl+shift+f9"):
            print("start")
            with sr.Microphone() as source:
                audio = r.listen(source)

                try:
                    text = r.recognize_google(audio, language='th')

                    print("Recognized Text:", text)  # Added print statement

                    print("Recognized Text:", text)  # Added print statement

                    if "เปิด Powerpoint" in text:
                        os.system('start POWERPNT.EXE')

                    if "เปิด Powerpoint" in text:
                        os.system('start POWERPNT.EXE')

                    if "เปิด Word" in text:
                        os.system("start WINWORD.EXE")

                    if "เปิด Word" in text:
                        os.system("start WINWORD.EXE")

                    if "เปิด YouTube" in text:
                        os.system("start https://youtube.com")

                    if "เปิด YouTube" in text:
                        os.system("start https://youtube.com")

                    if "เปิด discord" in text or "เปิดดิสคอร์ด" in text:
                        os.system('start discord')

                    if "เปิด discord" in text or "เปิดดิสคอร์ด" in text:
                        os.system('start discord')

                    if "เปิด Excel" in text:
                        os.system("start EXCEL.EXE")

                    if "เปิด Excel " in text:
                        os.system("start Excel")

                except sr.UnknownValueError:
                    print("ไม่สามารถรับรู้เสียงได้")
                except sr.RequestError as e:
                    print("พบข้อผิดพลาดจากการร้องขอ:", str(e))

run()