import speech_recognition as sr
import time
from gtts import gTTS
import os
import configparser
import threading
from playsound import playsound
from tkinter import *
import keyboard

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

Label2 = Label(window, text="", font=("Arial", 14), foreground="blue")
Label2.pack()

Label3 = Label(window, text="รายการคำสั่งที่พูดออกมา:", font=("Arial", 14), foreground="black")
Label3.pack()

command_list = Listbox(window, height=10, width=40, foreground="black", background="white")
command_list.pack()

# Function to convert text to speech and play the audio
def speak(text):
    tts = gTTS(text=text, lang="th")
    tts.save("audio.mp3")
    playsound("audio.mp3")
    os.remove("audio.mp3")

# Function to perform actions based on voice commands
def perform_action(text):
    command_list.insert(END, text)  # Add spoken command to the listbox

    if "เปิด Powerpoint" in text or "เปิดพาวเวอร์พอยท์" in text:
        os.system('start POWERPNT.EXE')
        Label1.config(text="เปิด Powerpoint")

    elif "เปิด Word" in text:
        os.system("start WINWORD.EXE")
        Label1.config(text="เปิด Word")

    elif "เปิด YouTube" in text:
        os.system("start https://youtube.com")
        Label1.config(text="เปิด YouTube")

    elif "เปิด discord" in text or "เปิดดิสคอร์ด" in text:
        discord = config.get("program", "discord")
        os.system(f'start {discord}')
        Label1.config(text="เปิด Discord")

    elif "เปิด Excel" in text:
        os.system("start EXCEL.EXE")
        Label1.config(text="เปิด Excel")

    elif "เปิดแชท gpt" in text:
        os.system("start https://chat.openai.com/")
        Label1.config(text="เปิดแชท GPT")

    elif "เปิด Facebook" in text:
        os.system("start https://www.facebook.com/")
        Label1.config(text="เปิด Facebook")

    elif "ลบไฟล์ขยะ" in text:
        os.system("del /q/f/s %TEMP%\*")
        Label1.config(text="ลบไฟล์ขยะ")

    elif "ปิดโปรแกรม" in text:
        exit()

    elif "เปิด 1" in text:
        program1 = config.get("program", "program1")
        os.system(f"start {program1}")
        Label1.config(text="เปิดโปรแกรม 1")

    elif "เปิด 2" in text:
        program2 = config.get("program", "program2")
        os.system(f"start {program2}")
        Label1.config(text="เปิดโปรแกรม 2")

    elif "เปิด 3" in text:
        program3 = config.get("program", "program3")
        os.system(f"start {program3}")
        Label1.config(text="เปิดโปรแกรม 3")

    elif "เปิด 4" in text:
        program4 = config.get("program", "program4")
        os.system(f"start {program4}")
        Label1.config(text="เปิดโปรแกรม 4")

    elif "เปิด 5" in text:
        program5 = config.get("program", "program5")
        os.system(f"start {program5}")
        Label1.config(text="เปิดโปรแกรม 5")

    elif "เปิดเว็บ" in text:
        Label1.config(text="พูด URL ที่ต้องการเปิด")
        listen_for_website()

    elif "หยุด" in text:
        global is_listening
        is_listening = False
        Label1.config(text="หยุดการรับคำสั่งด้วยเสียง")
        speak("หยุดการรับคำสั่งด้วยเสียง")
        

# Function to listen for website URL
def listen_for_website():
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='th')
        os.system(f"start https://{text}")
        Label1.config(text=f"เปิดเว็บ: {text}")
        start_button["state"] = "normal"
        Label2.config(text="เริ่มต้นการรับคำสั่งด้วยเสียง")
        speak(f"เปิดเว็บ: {text}")
    except sr.UnknownValueError:
        speak1 = "ไม่สามารถรับรู้เสียงได้"
        speak(speak1)
        Label1.config(text=speak1)
        start_button["state"] = "normal"
        Label2.config(text="ยังเริ่มต้นการรับคำสั่งด้วยเสียง")
    except sr.RequestError as e:
        speak1 = "พบข้อผิดพลาดจากการร้องขอ"
        speak(f"{speak1}: {str(e)}")
        Label1.config(text=speak1)
        start_button["state"] = "normal"
        Label2.config(text="ยังเริ่มต้นการรับคำสั่งด้วยเสียง")

# Function to start listening for voice commands
def start_listening():
    
    global is_listening
    is_listening = True
    Label2.config(text="เริ่มต้นการรับคำสั่งด้วยเสียง")
    start_button["state"] = "disabled"
    speak("เริ่มต้นการรับคำสั่งด้วยเสียง")
    Label2.config(text="เริ่มต้นการรับคำสั่งด้วยเสียง")

    def listening_thread():
        while is_listening:
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language='th')
                perform_action(text)
            except sr.UnknownValueError:
                speak("ไม่สามารถรับรู้เสียงได้")
                start_button["state"] = "normal"
                Label2.config(text="ยังเริ่มต้นการรับคำสั่งด้วยเสียง")
            except sr.RequestError as e:
                speak(f"พบข้อผิดพลาดจากการร้องขอ: {str(e)}")
                start_button["state"] = "normal"
                Label2.config(text="ยังเริ่มต้นการรับคำสั่งด้วยเสียง")
            finally:
                start_button["state"] = "normal"

    
    threading.Thread(target=listening_thread).start()

# Function to delete temporary files
def delete_temp_files():
    os.system("del /q/f/s %TEMP%\*")
    Label1.config(text="ลบไฟล์ขยะ")
    speak("ลบไฟล์ขยะ")

# Create GUI elements
start_button = Button(window, text="Start", width=25, font=("Arial", 16), command=start_listening, foreground="white", background="blue")
start_button.pack(pady=20)

delete_temp_button = Button(window, text="ลบไฟล์ขยะ %temp%", width=25, font=("Arial", 16), command=delete_temp_files, foreground="white", background="red")
delete_temp_button.pack(pady=10)

Label1 = Label(window, text="", font=("Arial", 14), foreground="black")
Label1.pack()

# Start the GUI event loop
window.mainloop()