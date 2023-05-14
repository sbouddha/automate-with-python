import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')  # Get the current speech rate

# Decrease the speech rate by 50 (adjust this value as needed)
engine.setProperty('rate', rate - 50)

engine.say("How much more time you need Pratima Kumari?")
engine.runAndWait()
