import pyttsx3
try:
    from termcolor import colored
except ImportError:
    print("Module 'termcolor' is not installed")
# Initialize the Text-to-Speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(speak_text: str, print_text: str = None):
    """Speak the given audio string."""

    print_text = print_text or speak_text
    try:
        cool_text = colored("[Friday] >>>", "cyan", attrs=["bold"])
        print(f'{cool_text} {print_text} \n')
    except:
        print(f'\n[Friday] >>>  {print_text} \n')
    engine.say(speak_text)
    engine.runAndWait()

