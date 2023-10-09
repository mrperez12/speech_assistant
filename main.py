import speech_recognition as sr
import time
import webbrowser
from time import ctime
import playsound
import os
import random
from gtts import gTTS


recongizer = sr.Recognizer()


def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            jarvis_speak(ask)
        audio = recongizer.listen(source)
        voice_data = ""
        try:
            voice_data = recongizer.recognize_google(audio, language="es-CL")
        except sr.UnknownValueError:
            jarvis_speak("Perdon, no entendi lo que dijiste")
        except sr.RequestError:
            jarvis_speak("Perdon, my servicio de discursos esta caido")
        return voice_data


def jarvis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='es')
    r = random.randint(1,10000000)
    audio_file = "audio_" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if "Cómo te llamas" in voice_data:
        jarvis_speak("Me llamo jarvis")
    if "qué hora es" in voice_data:
        jarvis_speak(ctime())
    if "Buscar" in voice_data:
        search = record_audio("¿Que quieres buscar?")
        url = "https://google.com/search?q=" + search
        webbrowser.open(url)
        jarvis_speak("ESto es lo que encontre para " + search)
    if "encontrar lugar" in voice_data:
        location = record_audio("¿Que lugar buscas?")
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.open(url)
        jarvis_speak("Aquí esta la ubicacion para " + location)
    if "salir" in voice_data:
        exit()
    if "cerrar firefox" in voice_data:
        os.system("pkill firefox")
        jarvis_speak("Firefox cerrado")
    if "abrir firefox" in voice_data:
        webbrowser.open("https://google.com/")
        jarvis_speak("Firefox abierto")
    

time.sleep(5)
jarvis_speak("Hola, ¿como te puedo ayudar?")
while 1:
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)