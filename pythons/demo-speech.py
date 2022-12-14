import speech_recognition as sr

# Set up the speech recognition object
r = sr.Recognizer()

# Start listening for input
with sr.Microphone() as source:
    audio = r.listen(source)

# Recognize the input
def sayHello():
    print("TODO Hello")

def sayGoodbye():
    print("TODO goodbye")


try:
    text = r.recognize_google(audio)

    # If the recognized text matches a specific keyword, trigger the corresponding function
    if text == "hello":
        sayHello()
    elif text == "goodbye":
        sayGoodbye()
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Error; {0}".format(e))
