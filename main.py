import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipedia
import webbrowser

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()

            if 'justice squad' in command:
                command=command.replace('justice squad','')
                print(command)
            
    except Exception as e:
        raise e
    
    return command

def run_assistant():
    command=take_command()
    print(command)

    if 'play' in command:
        song=command.replace('play','')
        speak('playing'+song)
        pywhatkit.playonyt(song)
    
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        speak('current time is'+time)
    
    elif 'name' in command:
        speak('my name is justice squad')

    elif 'joke' in command:
        speak(pyjokes.get_joke())
    
    elif 'wikipedia' in command:
        speak("searching wikipedia...")
        query=command.replace('wikipedia','')
        result=wikipedia.summary(query,sentences=5)
        speak("according to wikipedia")
        print(result)
        speak(result)
        


if __name__=="__main__":
    take_command()
    # speak("hey , this is justice squad here , tell me how can i help you ")
