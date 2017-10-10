import random,time
import pyttsx3
engine = pyttsx3.init()

while True:
    randomElever1 = random.randint(0,19)
    randomElever2 = random.randint(0 , 19)
    randomHandling = random.randint(0,7)
    elever = ["Yusuf","Omar","Said","Hudayfa","Hadi","Rasmus E","Liam","Mads","Oliver","Bjørn","Frederik L","Rasmus W","Jakob","Christoffer","Alexander","Michael","Gabriel","Allan","Daniel","Lasse"]
    handling = ["kissing","running","sitting","happy","nice","stupid","clever","drunk"]
    firstElev = elever[randomElever1]
    andenElev = elever[randomElever2]
    handlingElev = handling[randomHandling]

    samletTekst = firstElev + ' ' + 'and' + ' ' + andenElev + ' are ' + handlingElev
    time.sleep(random.randint(1,60))
    print(samletTekst)
    engine.say(samletTekst)
    engine.runAndWait()
