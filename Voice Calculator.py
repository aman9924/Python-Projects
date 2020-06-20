import pyttsx3
import datetime
import speech_recognition as sr

lst=[]
length=0
engine=pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
# print(voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def add():
    global temp
    temp=0
    for x in range(length):
        temp = temp + lst[x]
    return temp
def sub():
    global x
    global y
    try:
        x,y=lst
        return x-y
    except Exception as e:
        return "Sorry I cannot subtract more than two numbers"
def mul():
    global m
    m=1
    for x in range(length):
        m=m* lst[x]
    return m
def div():
    a,b=lst
    return a/b
def modulo():
    a,b=lst
    return a%b
def mini():
    return min(lst)
def maximum():
    return max(lst)
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning Aman")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Aman")
    else:
        speak("Good Evening Aman")
    print("Hello Aman I am your smart calculator, how can I help you")
    speak("Hello Aman I am your smart calculator, how can I help you")

def name():
    print("I am your smart calculator")
    speak("I am your smart calculator")
def time():
    strTime=datetime.datetime.now().strftime("%H:%M:%S")
    print(strTime)
    speak(f"The time is {strTime}")
    

def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        globals() ['lst'] = []
        print("Recognizing... ")
        query=r.recognize_google(audio,language='en-in')
        print("User said:  ",query)
        for words in query.split(' '):
            if words.isdigit():
                lst.append(eval(words))
        globals()['length'] = len(lst)
    except Exception as e:
        print("Please provide the input again.")
        speak("Please provide the input again.")
        return "None"
    return query




if __name__ == "__main__":
    wish()
    while (True):
        query = take_command().lower()
        if ("add" in query or "plus" in query or "addition" in query or "+" in query):
            result =f"Addition of given number is {add()}"
            print(result)
            speak(result)
        elif ("divide" in query or "divison" in query or "/" in query):
            result = f"Divison of given number is {div()}"
            print(result)
            speak(result)
        elif ("multiply" in query or "into" in query or "multiplication" in query or "product" in query or "*" in query):
            result = f"Multiplication of given number is {mul()}"
            print(result)
            speak(result)
        elif ("subtract" in query or "minus" in query or "subtraction" in query or "-" in query):
            result = f"Subtraction of given number is {sub()}"
            print(result)
            speak(result)
        elif ("min" in query or "minimun" in query or "smaller" in query):
            result = f"The smallest number in the given list is {mini()}"
            print(result)
            speak(result)
        elif ("max" in query or "maximum" in query or "largest" in query or "bigger" in query):
            result = f"The largest number in the given list is {maximum()}"
            print(result)
            speak(result)
        elif 'who' in query:
            name()

        elif 'time' in query:
            time()

        elif ("modulo" in query or "modulus" in query or "remainder" in query):
            result = f"Remainder is {modulo()}"
            print(result)
            speak(result)
        elif 'exit' in query or 'quit' in query or 'cancel process' in query:
            bye = "Thanks For Using Me...\nSee you Again"
            print(bye)
            speak(bye)
            quit()
