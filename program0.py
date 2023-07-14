import speech_recognition as sr
import time
from gtts import gTTS
import os
import configparser
import threading
from playsound import playsound
from tkinter import *

# Create a speech recognizer
r = sr.Recognizer()

# Load the configuration from the config.ini file
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

# Create a GUI window
window = Tk()
window.title("Voice Control")
window.geometry("300x200")

# Function to convert text to speech and play the audio
def speak(text):
    tts = gTTS(text=text, lang="th")
    tts.save("audio.mp3")
    playsound("audio.mp3")
    os.remove("audio.mp3")

# Function to perform actions based on voice commands
def perform_action(text):
    if "เปิด Powerpoint" in text or "เปิดพาวเวอร์พอยท์" in text:
        os.system('start POWERPNT.EXE')

    if "เปิด Word" in text:
        os.system("start WINWORD.EXE")

    if "เปิด YouTube" in text:
        os.system("start https://youtube.com")

    if "เปิด discord" in text or "เปิดดิสคอร์ด" in text:
        discord = config.get("program", "discord")
        os.system(f'start {discord}')

    if "เปิด Excel" in text:
        os.system("start EXCEL.EXE")

    if "เปิดแชท gpt" in text:
        os.system("start https://chat.openai.com/")

    if "เปิด Facebook" in text:
        os.system("start https://www.facebook.com/")

    if "ลบไฟล์ขยะ" in text:
        os.system("rd %temp% /s /q")

    if "ปิดโปรแกรม" in text:
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
            Label1.config(text="https อะไร")
            time.sleep(1)
            Label1.config(text="เริ่มพูด")
            audio = r.listen(source)
            
            r1 = sr.Recognizer()
            text1 = r1.recognize_google(audio, language='th')
            
            os.system(f"start https://{text1}")
            Label1.config(text=f"Recognized Text: {text1}")

# Function to listen for website URL
def listen_for_website():
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='th')
        os.system(f"start https://{text}")
    except sr.UnknownValueError:
        speak1 = "ไม่สามารถรับรู้เสียงได้"
        speak(speak1)
        Label1.config(text=speak1)
    except sr.RequestError as e:
        speak1 = "พบข้อผิดพลาดจากการร้องขอ"
        speak(f"{speak1}: {str(e)}")
        Label1.config(text=speak1)

# Function to start listening for voice commands
def start_listening():
    Label1.config(text="")
    speak("เริ่มต้นการรับคำสั่งด้วยเสียง")
    start_button["state"] = "disabled"

    def listening_thread():
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='th')
            perform_action(text)
        except sr.UnknownValueError:
            speak("ไม่สามารถรับรู้เสียงได้")
        except sr.RequestError as e:
            speak(f"พบข้อผิดพลาดจากการร้องขอ: {str(e)}")
        finally:
            start_button["state"] = "normal"

    threading.Thread(target=listening_thread).start()

# Create GUI elements
start_button = Button(window, text="Start", font=("Arial", 16), command=start_listening)
start_button.pack(pady=20)


Label1 = Label(window, text="", font=("Arial", 14))
Label1.pack()

# Start the GUI event loop
window.mainloop()
