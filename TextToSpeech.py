import pyttsx3
engine = pyttsx3.init()
while (True):

    engine.say("Mirsad, you are very nice")
    #engine.say(" Jeg vil gerne arbejde, men det gider jeg ikke")
    for i in range(10,-1,-1):
        text = str(i)
        engine.say(text)

    engine.say("Fuck off ")
    engine.runAndWait()



