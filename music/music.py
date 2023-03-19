from pytube import YouTube
import pyttsx3


engine = pyttsx3.init()
test = ('enter the link below you idiot')
engine.say(test)
engine.runAndWait()


link = str(input())
yt = YouTube(link)

#""" stream = yt.streams.get_highest_resolution() for video as well """
#""" for music only """
stream = yt.streams.filter(only_audio=True).first()
stream.download()

test = ('download finished')
engine.say(test)
engine.runAndWait()