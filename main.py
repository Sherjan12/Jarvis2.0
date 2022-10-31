import keyboard
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pyautogui
import os
import webbrowser
import time
import multiprocessing

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.setProperty('rate', 185)

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! Sir")
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon! Sir')
    else:
        speak('Good Evening! Sir')
    speak('I am Jarvis and now I am online')


def takingcommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        # r.pause_threshold = 1
        r.energy_threshold = 1150
        audio = r.listen(source)
    try:

        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        speak(f"User said: {query}\n")
    except Exception:

        speak('I do not understand Sir!')# Say that again will be printed in case of improper voice


        return "None"  # None string will be returned
    return query


def sleepingcommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        r.energy_threshold = 1100
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.
    except Exception:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice

        return "None"  # None string will be returned
    return query


def yt():

    try:

        speak('What should I search Sir!')
        search = takingcommand().lower()
        speak('Searching...')
        webbrowser.open_new_tab('https://www.youtube.com/')
        time.sleep(6)
        pyautogui.moveTo(474, 133)

        pyautogui.click()
        pyautogui.typewrite(search)
        time.sleep(2)
        pyautogui.moveTo(966, 123)
        pyautogui.click()

    except Exception:
        print('error')


def restore():

    pyautogui.getWindowsWithTitle('C:\Windows\py.exe')[0].restore()


def minimize():
    pyautogui.getWindowsWithTitle('C:\\Windows\\py.exe')[0].minimize()


def task():

    while True:
        query = takingcommand().lower()
        if 'hello jarvis' in query or 'hi jarvis' in query:
            speak('hello Sir! How are you')
        if 'i am fine jarvis' in query or 'i am fine' in query:
            speak('I hope that you are always fine')
        if 'what is your name' in query:
            speak('my name is jarvis')

        elif 'hand free mode' in query:
            try:
                pyautogui.press('volumedown')
                pyautogui.moveTo(85, 141)
                pyautogui.click()
                pyautogui.sleep(1)
                pyautogui.moveTo(100, 200)
            except Exception:
                print('error')

        elif 'wait' in query:
            try:

                speak('How many seconds,Sir')
                w = int(takingcommand().lower())
                speak(f'Ok sir I am gonna wait  {w} seconds')
                pyautogui.sleep(w)
            except:
                print('error')


        elif 'Who you work for' in query or 'who is your master' in query:
            speak('I work for SJBravo')
        elif 'who is SJBravo' in query:
            speak('He is 16 years old boy and he is very intelligent')
        if 'get title' in query:
            v = pyautogui.getActiveWindowTitle()
            print(v)
        if 'full screen' in query:
            pyautogui.press('f')
        if 'normal screen' in query:
            pyautogui.press('f')

        elif 'speed' in query:
            try:
                os.system('cmd /k "speedtest')
            except:
                speak("there is no internet connection")


        if 'wikipedia' in query or 'search wikipedia' in query:
            # engine.setProperty('rate', 200)
            speak('Searching...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('opening youtube...')
            webbrowser.open_new_tab('https://www.youtube.com/')

        elif 'open google' in query:
            speak('opening google...')
            webbrowser.open_new_tab("https://www.google.com/")

        elif 'open game' in query:
            try:
                import time
                speak("opening Game...")
                os.startfile("C:\\Users\\Jan's\\AppData\\Roaming\\.minecraft\\TLauncher.exe")
                time.sleep(32)
                pyautogui.moveTo(801, 669)
                pyautogui.click()
                time.sleep(15)
                pyautogui.moveTo(678, 503)
                pyautogui.click()
                pyautogui.sleep(20)
            except Exception:
                print(Exception)

        elif 'open code' in query or 'open pycharm' in query:
            speak('opening PYCharm')
            os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.2\\bin\\pycharm64.exe")

        elif 'sleep' in query:
            speak('I will be in listening mode')
            minimize()
            break

        elif "what is time now" in query or 'tell the time' in query:
            now = datetime.datetime.now().strftime('%I:%M:%p')
            speak('Sir! time is')
            speak(now)

        elif 'take screenshot' in query or 'take picture' in query:
            import time
            speak('Sir!what should I name screenshot')
            name = takingcommand().lower()

            img = pyautogui.screenshot()
            time.sleep(3)
            img.save(f"{name}.png")
            speak('Sir!screenshot has been saved')

        elif 'shutdown' in query:
            speak('sir system will be shutdown in 2 sec')
            os.system('shutdown /s')

        elif 'goodbye jarvis' in query or 'quit jarvis' in query:
            speak('Goodbye sir!')
            quit()

        elif 'search on youtube' in query:
            yt()
        elif 'mute' in query:
            pyautogui.press('volumemute')

        elif 'unmute' in query:
            pyautogui.press('volumemute')

        elif 'open server' in query:
            speak('ok, Opening server')
            webbrowser.open('https://aternos.org/servers/')

        elif 'single player' in query:
            pyautogui.moveTo(672, 364)
            pyautogui.click()
            pyautogui.sleep(2)

        elif 'write id' in query:
            pyautogui.typewrite('hermitcraftseason7id')

        elif 'world one' in query:
            pyautogui.moveTo(324, 194)
            pyautogui.click()

        elif 'world2' in query:
            pyautogui.moveTo(327, 303)
            pyautogui.click()

        elif 'multiplayer' in query:
            pyautogui.moveTo(673, 435)
            pyautogui.click()
            pyautogui.sleep(2)

        elif 'server1' in query:
            pyautogui.moveTo(296, 140)
            pyautogui.click()

        elif 'server2' in query:
            pyautogui.moveTo(293, 254)
            pyautogui.click()

        elif 'open chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'video one' in query:
            pyautogui.moveTo(317, 313)
            pyautogui.click()

        elif 'video two' in query:
            pyautogui.moveTo(423, 536)
            pyautogui.click()

        elif 'video three' in query:
            pyautogui.moveTo(444, 664)
            pyautogui.click()
        elif 'side 1' in query:
            pyautogui.moveTo(1000, 241)
            pyautogui.click()

        elif 'side 2' in query:
            pyautogui.moveTo(1000, 371)
            pyautogui.click()

        elif 'side 3' in query:
            pyautogui.moveTo(1000, 460)
            pyautogui.click()

        if 'restore' in query:
            restore()


if __name__ == "__main__":
    wish()
    task()



if keyboard.read_key() == "`":
    print("A Key Pressed")
    restore()
    task()
