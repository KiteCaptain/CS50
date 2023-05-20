#  This script does not run on Wsl
import pyttsx3 as pt 

pt.init(driverName='espeak')
engine = pt.init()
name = input("What's your name?")
engine.say(f"Hello, {name}")
engine.runAndWait()