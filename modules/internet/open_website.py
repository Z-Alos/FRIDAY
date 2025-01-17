import webbrowser
from core.engine import speak

def open_this_thing(url, name):
    try:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
        webbrowser.get('chrome').open(url)
        speak(f"Opening {name}.")
    except Exception as e:
        print(f"Error opening {name}: {e}")
        speak(f"Couldn't open {name}. Please check your browser path or network.")

def open_website(command):
    """Open a website in Chrome."""
    
    if "youtube" in command:
        open_this_thing("https://youtube.com", "Youtube")
    elif 'google' in command:
        open_this_thing("https://google.com", "Google")
    elif 'whatsapp' in command:
        open_this_thing("https://web.whatsapp.com", "Whatsapp")
    elif 'chat' in command:
        open_this_thing("https://chatgpt.com", "ChatGPT")

    