#####
##### Ф.И: Ноурузи Мехди
##### ИСУ: 317306
##### группа: R3135
#####Номер варианта: 6
#####


import requests
import speech_recognition as sr
import pyttsx3
import json


r = sr.Recognizer()
engine = pyttsx3.init()


def handle_command(command):
    if command == "start":
        try:
            response = requests.get("https://www.boredapi.com/api/activity")
            data = response.json()
            activity = data["activity"]
            engine.say(f"Your random activity is {activity}")
            engine.runAndWait()
        except:
            engine.say("Sorry, there was an error in the request.")
            engine.runAndWait()
    elif command == "name":
        response = requests.get("https://www.boredapi.com/api/activity")
        data = response.json()
        activity = data["type"]
        engine.say(f"The name of activity is {activity}")
        engine.runAndWait()
    elif command == "participants":
        try:
            response = requests.get("https://www.boredapi.com/api/activity")
            data = response.json()
            participants = data["participants"]
            engine.say(f"You need {participants} participants.")
            engine.runAndWait()
        except:
            engine.say("Sorry, there was an error in the request.")
            engine.runAndWait()
    elif command == "next":
        engine.say("The next lesson is about Python programming.")
        engine.runAndWait()
    elif command == "save":
        try:
            response = requests.get("https://www.boredapi.com/api/activity")
            data = response.json()
            activity = data["activity"]
            participants = data["participants"]
            activity_dict = {
                "activity": activity,
                "participants": participants
            }
            with open("activity.json", "w") as f:
                json.dump(activity_dict, f)
            engine.say("Activity data saved to file.")
            engine.runAndWait()
        except:
            engine.say("Sorry, there was an error in saving the activity data.")
            engine.runAndWait()
    else:
        engine.say("Sorry, I didn't understand what you said.")
        engine.runAndWait()


while True:
    with sr.Microphone() as source:
        print("Speak now...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print(f"Recognized command: {command}")
        handle_command(command.lower())
    except sr.UnknownValueError:
        engine.say("Sorry, I didn't understand what you said.")
        engine.runAndWait()
    except sr.RequestError:
        engine.say("Sorry, my speech recognition service is down.")
        engine.runAndWait()
