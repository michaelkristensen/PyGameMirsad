import random
import pyttsx3
import time


engine = pyttsx3.init()

aWordList = ['Mirsad ','Mette ','Alma ','Emil ','Bella ']

bWordList = ['is ','going ','slipping ','running ','working ','singing ','talking ','jumping ']

cWordList = ['in school ','at home ','on holiday ','in bus ']

while (True):
    aWordNum = random.randint(0,4)

    bWordNum = random.randint(0,7)

    cWordNum = random.randint(0,3)


    aWord = aWordList[aWordNum]

    bWord = bWordList[bWordNum]

    cWord = cWordList[cWordNum]



    textWord = aWord + bWord + cWord

    engine.say(textWord)
    engine.runAndWait()

    time.sleep(random.randint(1,500))


#print(textWord)
