import os
from datetime import datetime


def set_alarm(alarm_time, sound_file='alarm.wav', message='Wake up!'):
    try:
        alarm = datetime.strptime(alarm_time, '%d.%m.%Y %H:%M')
        while True:
            current_time = datetime.now()
            if current_time.time() >= alarm.time():
                os.system(sound_file)
                print(message)
                break
    except ValueError:
        print('Incorrect time format. Please try: dd.mm.yyyy h:m')


if __name__ == '__main__':
    set_alarm('22.10.2020 22:49')
