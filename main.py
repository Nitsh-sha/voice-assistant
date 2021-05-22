import pyttsx3
import speech_recognition as sr
from nltk.tokenize import word_tokenize
import VoiceAuth
import VoiceDB
import Actions
import sys


engine = pyttsx3.init()
PHRASE = 'never forget tomorrow is a new day'

def record_audio():
    """
        Recording audio and saving it on the disk
        VoiceIt2 API requires audio file
    """
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            with open("microphone-results.wav", "wb") as f:
                f.write(audio.get_wav_data())
            return "./microphone-results.wav"
        except Exception as e:
                print(e)
                speak(engine, "Could you please repeat what you just said for me?")


def authenticate():
    
    """
        Method to authenticate the user
        Create user if user does not exists
        If user exists, authenticate against the registered voice phrase
    """
    # Authentication for the user - 
    # Name will be asked, if that name is in database then
    # we will fetch the user id against that name
    # And then voice authentication from VoiceIt2 API
    speak("Let's do the authentication")
    speak("Say your name")
    name = takeCommandMic()
    name = name.lower()
    print(name)

    # VoiceDB object
    vdb = VoiceDB.VoiceDB
    uid = vdb.getUser(name)
    print(uid)
    if uid == None:
        speak("Looks like you are not registered")
        # Press something if you want to get registered
        uid = VoiceAuth.create_user()
        if uid:
            for i in range(0,3):
                speak("Please speak your authentication phrase")
                audio = record_audio()
                res = VoiceAuth.register_voices(uid,audio)
                print(res)

            res = vdb.insertUser(name,uid)
            print(res)
            speak("Successfully registered")
            return True
        else:
            raise Exception
    else:
        speak("Alright  " + name)
        speak("Please speak your authentication phrase")
        audio = record_audio()
        auth = VoiceAuth.verify(uid, audio)
        if auth:
            speak("Verification Successful")
            return True
        else:
            speak("Verification Failed")
            return False
    
def speak(audio):

    # Speaking out the text
    engine.say(audio)
    engine.runAndWait()

def setvoices(voice):

    """
        Set voice for the voice engine
    """
    voices = engine.getProperty('voices')
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        speak("hello this is Tom")
    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        speak("hello this is Natasha")

def takeCommandMic():
    
    """
        Listen to audio and convert to text
    """
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        
        try:
            query = r.recognize_google(audio, language='en-GB')
            print(query)
            return query
        except Exception as e:
            print(e)
            speak("Could you please repeat what you just said for me?")


def main():
    setvoices(1)
    wakeword = "tom"
    if authenticate():
    # if True:
        speak("How shall I help you")
        while True:
            query = takeCommandMic().lower()
            query = word_tokenize(query)
            print(query)
            if wakeword in query:
                if 'get' in query:
                    if 'emails' in query:
                        Actions.fetch_emails(engine)
                    elif 'messages' in query:
                        Actions.fetch_messages(engine)
                    elif 'wikipedia' in query:
                        Actions.fetch_wiki(engine)
                    elif 'google' in query or 'search' in query:
                        Actions.fetch_search(engine)
                    elif 'youtube' in query:
                        Actions.fetch_youtube(engine)
                    elif 'weather' in query:
                        Actions.fetch_weather(engine)
                    elif 'news' in query:
                        Actions.fetch_news(engine)
                    elif 'websites' in query:
                        Actions.fetch_web(engine)
                    elif 'pending' in query and 'notes' in query:
                        Actions.pendingnotes(engine)
                    elif 'notes' in query:
                        Actions.fetch_notes(engine)    
                    else:
                        pass    
                else:
                    if 'time' in query:
                        Actions.time(engine)
                    elif 'date' in query:
                        Actions.date(engine)
                    elif 'email' in query:
                        Actions.sendEmail(engine)
                    elif 'message' in query:
                        Actions.sendwhatsmsg(engine)
                    elif 'wikipedia' in query:
                        Actions.wikipedia(engine)
                    elif 'search' in query:
                        Actions.searchgoogle(engine)
                    elif 'youtube' in query:
                        Actions.youtubeplay(engine)
                    elif 'weather' in query:
                        Actions.weather(engine)
                    elif 'news' in query:
                        Actions.news(engine)
                    elif 'website' in query:
                        Actions.openwebsite(engine)
                    elif 'read' in query:
                        Actions.text2speech(engine)
                    elif 'covid' in query:
                        Actions.covid(engine)
                    elif 'joke' in query:
                        Actions.jokes(engine)
                    elif 'screenshot' in query:
                        Actions.screenshot(engine)
                    elif 'take' in query or 'write' in query or 'note' in query:
                        Actions.note(engine)
                    elif 'pending' in query or  'tasks' in query:
                        Actions.pendingnotes(engine)
                    elif 'password' in query:
                        Actions.passwordgen(engine)
                    elif 'close' in query:
                        quit()
                    else:
                        pass


if __name__ == "__main__":
    main()        