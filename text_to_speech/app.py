import pyttsx3

engine = pyttsx3.init()

while True:
    answer = input("Enter your text: \n")
    engine.say(answer)
    engine.runAndWait()