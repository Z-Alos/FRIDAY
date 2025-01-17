import datetime
from core.engine import speak

def wish_me():
    """Greet the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning, Zaalos!")
    elif 12 <= hour < 18:
        speak("Good Afternoon, Zaalos!")
    else:
        speak("Good Evening, Zaalos!")
