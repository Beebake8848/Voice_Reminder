import time
import pyttsx3

def notify(title, message):
    engine = pyttsx3.init()
    
    engine.say(title)
    engine.say(message)

    engine.runAndWait()

if __name__ == "__main__":
    while True:
        notify("Notification", "Hey Bibek, drink water")

        time.sleep(60*120)
