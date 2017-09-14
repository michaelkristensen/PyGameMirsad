import pyttsx3
engine = pyttsx3.init()
engine.say("Mirsad, you are very nice ")
for i in range(10,-1,-1):
    text = str(i)
    engine.say(text)

engine.say("Fuck off ")
engine.runAndWait()



