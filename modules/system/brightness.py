from core.engine import speak
import screen_brightness_control as sbc

current_brightness = sbc.get_brightness()

def set_brightness_level(level):
    sbc.set_brightness(level)
    speak(f"Brightness set to {level}%")

def increase_brightness():
    sbc.set_brightness('+10')
    speak("Brightness increased by 10%")
    
def decrease_brightness():
    sbc.set_brightness('-10')
    speak("Brightness decreased by 10%")

def change_brightness(command):
    level = ''.join(filter(str.isdigit, command))
    if level:
        set_brightness_level(level)
    elif "increase" in command:
        increase_brightness()
    elif "decrease" in command:
        decrease_brightness()
