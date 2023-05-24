import speech_recognition
recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something....")
    audio = recognizer.listen(source)

print("You said:")
words = recognizer.recognize_google(audio)

if "hello" in words:
    print("Hello to you too!")
elif "how are you" in words:
    print("Am good, thanks for asking.")
elif "goodbye" in words:
    print("Goodbye to you too see you soon!")
else: 
    print("Huh!?")