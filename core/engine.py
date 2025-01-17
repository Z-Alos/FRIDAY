import pyttsx3

# Initialize the Text-to-Speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    """Speak the given audio string."""
    engine.say(audio)
    engine.runAndWait()
