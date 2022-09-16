import pyttsx3
import speech_recognition as sr
import datetime

def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
    pass
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Just say the magic word! and i will get it done!")

def takeCommand():
    #It takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


sayhellototheworld = """engine = pyttsx3.init()
engine.say("Hello World!")
engine.runAndWait()"""
testmytypingspeed = """from time import time

print()
print("NO NEW LINE IS THERE, WRITE CONTINUOUSLY(just SPACES)")
s = "this is a simple paragraph that is meant to be nice and" \
    " easy to type which is why there will be no commas no periods " \
    "or any capital letters so i guess this means that it cannot really " \
    "be considered a paragraph but just a series of sentences"
words = (len(s.split()))

print(s)

print("After you are done press enter to know your time and speed")
input("Press any key to Start:")

try:
    print("Timer Started")
    start = time()
    t = input()
    end = time()
    if t == s:
        total = round(end - start, 2)
        print("Voila you typed that correctly")
        print("Your time was %s seconds" % total)
        total = int(total) / 60
        print("Speed was %s wpm" % (str(words // total)))

    else:
        print("Wrongly entered")
        print("Try again")

except KeyboardInterrupt:
       print("")
"""
while True:

    query = takeCommand().lower
    if query == "test my typing speed":
        engine = pyttsx3.init()
        engine.say("Of course , please attend this session on the console")
        engine.runAndWait()
        exec(testmytypingspeed)
    elif query == "say hello to the world":
        exec(sayhellototheworld)
    else:
        print("You have not taught me that yet")

while True:
    engine = pyttsx3.init()
    engine.say("Anything more ?")
    engine.runAndWait()

    r = sr.Recognizer()
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
    response1 = text

    sayhellototheworld = """engine = pyttsx3.init()
engine.say("Hello World!")
engine.runAndWait()"""
    testmytypingspeed = """from time import time

print()
print("NO NEW LINE IS THERE, WRITE CONTINUOUSLY(just SPACES)")
s = "this is a simple paragraph that is meant to be nice and" \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        " easy to type which is why there will be no commas no periods " \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            "or any capital letters so i guess this means that it cannot really " \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            "be considered a paragraph but just a series of sentences"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        words = (len(s.split()))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        print(s)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        print("After you are done press enter to know your time and speed")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        input("Press any key to Start:")

    try:
        print("Timer Started")
        start = time()
        t = input()
        end = time()
        if t == s:
            total = round(end - start, 2)
            print("Voila you typed that correctly")
            print("Your time was %s seconds" % total)
            total = int(total) / 60
            print("Speed was %s wpm" % (str(words // total)))

        else:
            print("Wrongly entered")
            print("Try again")

    except KeyboardInterrupt:
    print("")
    """

    if response1 == "That's all buddy":
        engine.say("Ok , feel free to call me anytime")
    elif response1 == "test my typing speed":
        engine = pyttsx3.init()
        engine.say("Of course, please attend this session on the console")
        engine.runAndWait()
        exec(testmytypingspeed)
    elif response1 == "say hello to the world":
        exec(sayhellototheworld)
    elif response1 == "":
        continue
    else:
        print("You have not taught me that yet")


