from core.listener import recognize_speech
from core.command_handler import handle_command
from core.utilities import wish_me
import multiprocessing

def main():
    """Main function to run the voice assistant."""
    # Create a queue for inter-process communication
    queue = multiprocessing.Queue()

    # Start the speech recognition process
    speech_process = multiprocessing.Process(target=recognize_speech, args=(queue,))
    speech_process.start()

    print("Main process is running...")
    wish_me()

    try:
        while True:
            if not queue.empty():
                query = queue.get().lower()
                print(f"Recognized: {query}")

                handle_command(query)

    except KeyboardInterrupt:
        print("Stopping assistant...")
        speech_process.terminate()
        speech_process.join()

if __name__ == "__main__":
    main()
