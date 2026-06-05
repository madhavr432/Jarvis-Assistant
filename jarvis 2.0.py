from googletrans import Translator 
import webbrowser
import pyttsx3
import pywhatkit
import os
import speech_recognition as sr
import wikipedia
import pyautogui
import keyboard
import pyjokes          
from AppOpener import run
import datetime
from playsound import playsound
import sounddevice as sd
import speech_recognition as sr


Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')

Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',150)
def Speak(audio):
    print("  ")
    Assistant.say(audio)
    print("  ")
    print(f": {audio}")
    Assistant.runAndWait()
    
 
def takecommand():
    recognizer = sr.Recognizer()
    fs = 44100       # Sample rate
    duration = 5     # seconds to record

    print("Listening...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    # Convert numpy array to AudioData for speech_recognition
    audio_data = sr.AudioData(recording.tobytes(), fs, 2)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio_data, language='en-in')
        print(f"You said: {query}")
    except Exception as e:
        print("Say it again...")
        return "none"
    return query.lower()
def TaskExe():
    def Music ():
        Speak('tell me the name of the song')
        musicName = takecommand()
        if'play' in musicName:
            os.startfile('D:\\python\\play.ogg')
        elif 'f' in musicName:
            os.startfile('D:\\python\\f.mp3')
        elif 'right' in musicName:
            os.startfile('D:\\python\\right.mp3')
        else:
            pywhatkit.playonyt(musicName)
        Speak("Your song has been started, enjoy sir!")
    def youtubeauto():
        Speak("What's your command?")
        comm = takecommand()
        if 'pause' in comm:
            keyboard.press('space bar')
        elif 'restart' in comm:
            keyboard.press('0')
        elif 'mute' in comm:
            keyboard.press('m')
        elif 'skip' in comm:
            keyboard.press('l')
        elif 'back' in comm:
            keyboard.press('j')
        elif 'full screen' in comm:
            keyboard.press('f')
        elif 'film mode' in comm:
            keyboard.press('t')
        Speak("done sir!")
    def takehindi():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            command.pause_threshold = 1
            audio = command.listen(source)
            try:
                print("recognizing")
                query = command.recognize_google(audio,language='hi')
                print(f"you said : {query}")
            except Exception as Error:
                print("say it again")
                return "none"
            return query.lower()
    def tran():
        Speak("Tell me the line!")
        line = takehindi()
        Traslate = Translator()

        result = Traslate.translate(line)
        Text = result.text
        Speak(Text)


    while True:
        query = takecommand()
        if 'hello'in query:
            Speak("hello sir ,I am jarvis")
            Speak("your personal AI assistant")
            Speak("how may I help you")  
        elif 'how are you' in query:
            Speak("I am fine sir , what's about you")
        elif 'you need a break' in query:
            Speak("ok sir, you can call me anytime")
            break
        elif 'bye' in query:
            Speak("ok bye sir")
            break
        elif 'youtube search' in query:
            Speak("ok sir this is what I found for your search")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done Sir!")
        elif 'google search' in query:
            Speak("This is What I found for your search sir!  ")
            query= query.replace("jarvis","")
            query= query.replace("google search","")
            pywhatkit.search(query)
            Speak("Done sir!")
        elif 'website' in query:
            Speak("ok sir! , lauching...")
            query= query.replace("jarvis","")
            query= query.replace("website","")
            web1= query.replace("open","")
            web2 = 'https://www.'+ web1 +'.com'
            webbrowser.open(web2)
            Speak("launched!")
        elif 'launch' in query:
            Speak("tell me the name of the website!")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done sir!")
        elif'pw' in query:
            Speak("ok sir!")
            webbrowser.open("https://www.pw.live/study/batches")
            Speak("Done sir!")
        elif'open youtube' in query:
            Speak("ok sir!")
            webbrowser.open("https://www.youtube.com")
            Speak("Done sir!")
        elif 'music' in query:
            Music()
        elif 'wikipedia' in query:
            Speak("ok sir! , lauching...")
            query= query.replace("jarvis","")
            query= query.replace("wikipedia","")
            wiki= wikipedia.summary(query,2)
            Speak(f"according to wikipedia : {wiki}")
        elif 'screenshot' in query:
            Speak("name your file")
            path = takecommand()
            path1name = path + ".png"
            path1 = r"C:\Users\madha\OneDrive\चित्र\Screenshots\\" + path1name
            kk = pyautogui.screenshot()
            kk.save(path1)
            os.startfile(r"C:\Users\madha\OneDrive\चित्र\Screenshots\\")
            Speak("Here is your screenshot")

        elif 'open' in query:
            query= query.replace("open","")
            pyautogui.sleep(2)
            pyautogui.press("enter") 
        elif 'whatsapp munna' in query:
            Speak("tell me the message")
            msg = takecommand()
            Speak("tell me time in hours")
            hour = int(takecommand())
            Speak("tell me time in minutes")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+919153810109",msg,hour,min)
        elif 'whatsapp mummy' in query:
            Speak("tell me the message")
            msg = takecommand()
            Speak("tell me time in hours")
            hour = int(takecommand())
            Speak("tell me time in minutes")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+919934673317",msg,hour,min)
        elif 'whatsapp papa' in query:
            Speak("tell me the message")
            msg = takecommand()
            Speak("tell me time in hours")
            hour = int(takecommand())
            Speak("tell me time in minutes")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+918409973950",msg,hour,min)
        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/@12.9539974,77.6309395,11z')
            Speak("Done sir!")
        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")
            Speak("your command has been succesfully compleated!")
        elif 'close mic' in query:
            os.system("taskkill /f /im WOMicClient.exe")
            Speak("your command has been succesfully compleated!")
        elif 'close edge' in query:
            os.system("taskkill /f /im msedge.exe")
            Speak("your command has been succesfully compleated!")
        elif 'close notepad' in query:
            os.system("taskkill /f /im notepad.exe")
            Speak("your command has been succesfully compleated!")
        elif 'close code' in query:
            os.system("taskkill /f /im code.exe")
            Speak("your command has been succesfully compleated!")
        elif 'close files' in query:
            os.system("taskkill /f /im explorer.exe")
            Speak("your command has been succesfully compleated!")
        elif 'close calculator' in query:
            os.system("taskkill /f /im Calculator.exe")
            Speak("your command has been succesfully compleated!")
        elif 'pause' in query:
            keyboard.press('k')
            Speak("done sir!")
        elif 'restart' in query:
            keyboard.press('0')
            Speak("done sir!")
        elif 'mute' in query:
            keyboard.press('m')
            Speak("done sir!")
        elif 'skip' in query:
            keyboard.press('l')
            Speak("done sir!")
        elif 'back' in query:
            keyboard.press('j')
            Speak("done sir!")
        elif 'full screen' in query:
            keyboard.press('f')
            Speak("done sir!")
        elif 'film mode' in query:
            keyboard.press('t')
            Speak("done sir!")
        elif 'youtube tools' in query:
            youtubeauto()
            Speak("done sir!")
        elif 'close tab' in query:
            keyboard.press_and_release('ctrl + w')
            Speak("done sir!")
        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + w')
            Speak("done sir!")
        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')
            Speak("done sir!")
        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')
            Speak("done sir!")
        elif 'jokes' in query:
            get = pyjokes.get_joke()
            Speak(get)
        elif 'repeat my words' in query:
            Speak("speak sir!")
            jj=takecommand()
            Speak(f"you said : {jj}")
        elif 'my location' in query:
            Speak("ok sir, wait a second")
            webbrowser.open('https://www.google.co.in/maps/@25.6689872,85.832492,219m/data=!3m1!1e3')
            Speak("done sir!")
        elif 'ok' in query :
            keyboard.press('enter')
        elif 'alarm' in query:
            Speak("enter the time!")
            time = input(":enter the time:")
            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")
                if now == time:
                    Speak("time to wake up sir")
                    playsound('right.mp3')
                    Speak("Alarm closed")
                elif now>time:
                    break
        elif 'translate' in query:
            tran()
            




        
TaskExe()
    
