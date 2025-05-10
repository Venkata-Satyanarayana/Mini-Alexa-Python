import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyautogui
import pyaudio

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            talk('hi sir please tell me how can i help you')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        time = ('Current time is ' + time)
        print(time)
        talk(time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        joke = (pyjokes.get_joke())
        print(joke)
        talk(joke)
    elif 'open' in command:
        command = command.replace('open', '')
        pyautogui.press('super')
        pyautogui.typewrite(command)
        pyautogui.sleep(2)
        pyautogui.press('enter')
    else:
        talk('Please say the command again.')


while True:
    try:
        run_alexa()
    except UnboundLocalError:
        print('No command detected!')
        break
