import speech_recognition as sr
from multiprocessing import Queue
from core.engine import speak

def recognize_speech(queue: Queue):
    """Recognize speech and send the recognized text to a queue."""
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Speech recognition process started...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        while True:
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                queue.put(text)
            except sr.UnknownValueError:
                queue.put("Could not understand the audio")
            except sr.RequestError:
                error_message = "Could not connect to the internet, check your connectivity..."
                speak(error_message)
                queue.put(error_message)
