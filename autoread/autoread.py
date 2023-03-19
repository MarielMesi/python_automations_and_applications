import pyttsx3

engine = pyttsx3.init()
test = ('type what you would like me to read')
engine.say(test)
engine.runAndWait()

txt = input()
engine.say(txt)
engine.runAndWait()
