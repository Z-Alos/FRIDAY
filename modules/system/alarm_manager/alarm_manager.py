# !todo()
# implement priorty queue + avl/red black
from datetime import datetime
import json
from core.command_handler import handle_command

ALARM_FILE = "alarm.json"

def alarm_manager(command):
    create_alarm(command)

def create_alarm(command):
    alarm_time = datetime.strptime(command, '%I:%M %p')
    alarm_data = {
         'id': datetime.now().isoformat(),
         'time': alarm_time.strftime('%I:%M %p'),
         'activity': 'none'  
    }

    alarm = load_alarms()
    alarm.append(alarm_data)
    save_alarm(alarm)

def load_alarms():
    try:
        with open(ALARM_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def save_alarm(alarm_data):
    with open(ALARM_FILE, 'w') as f: # change it to append mode
        json.dump(alarm_data, f, indent=4)

def just_beat_it(alarm):
    print("Alarm Ringing...")
    if(alarm['activity'] == 'wakeup_protocol'):
        print(alarm['activity'])
        handle_command("fan")

# command = input("Input Alarm: ")
# alarm_manager(command)




