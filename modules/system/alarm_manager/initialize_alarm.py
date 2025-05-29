from datetime import datetime
from alarm_manager import just_beat_it, load_alarms
import threading
import time

all_alarms = load_alarms()

def initialize_alarm(alarm):
    timeLeft = datetime.now().strftime("%I:%M %p")
    currentTime = datetime.strptime(timeLeft, "%I:%M %p")
    alarmTime = datetime.strptime(alarm['time'], "%I:%M %p")

    timeDiff = alarmTime - currentTime
    print(timeDiff.total_seconds())
    time.sleep(timeDiff.total_seconds())
    just_beat_it(alarm);

for alarm in all_alarms:
    threading.Thread(target=initialize_alarm, args=(alarm,)).start()


