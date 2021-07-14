#!/usr/bin/env python3

from time import sleep, time
from tkinter.constants import TOP
from pynput import keyboard
import speech_recognition as sr
import tkinter as tk
from tkinter import Pack, filedialog, Text
import threading
from pynput.keyboard import Key, Controller

from read import request, terminate

import sys


keyboard = Controller()
listening = False
remote = True

def listen():
    global listening
    global remote

    if listening == True:

        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

    # recognize speech using Sphinx
    """
    try:
        print("Sphinx API: " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
    """

    if listening == True:
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            query = r.recognize_google(audio, language="de-DE")
            print("Google API: " + query)

            query = query.lower()

            if 'test' in query:
                commandRight()

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    else:
        if remote == True:
            request()
            sleep(1)

def startThread():
    thread = threading.Thread(target=startRecognition)
    thread.daemon = True
    thread.start()

def startRecognition():
    global listening
    while True:  
        listen()

def runApp():
    global listening
    listening = True
    print("Recognition started")

def stopApp():
    global listening
    listening = False

    print("Recognition stopped")

def enableListener():
    global listening
    listening = True

def disableListener():
    global listening
    listening = False

def commandRight():
    print('Trigger: right')
    keyboard.press(Key.right)
    keyboard.release(Key.right)

def commandLeft():
    print('Trigger: left')
    keyboard.press(Key.left)
    keyboard.release(Key.left)


startThread()

root = tk.Tk()
root.title("SpeechControl")

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

runApp = tk.Button(root, text="Start Speech-Recognition", padx=10, pady=10, fg="white", bg="#263D42", command=runApp)
runApp.pack()

stopApp = tk.Button(root, text="Stop Speech-Recognition", padx=10, pady=10, fg="white", bg="#263D42", command=stopApp)
stopApp.pack()

root.mainloop()
