import time
import os
from playsound import playsound

os.chdir('C://Users//AkshatPanda//Desktop//A.R.I.S.E//timer')
custom_permission = input('do you want to do a custom timer:')
if custom_permission == 'no':
    hours = int(input('enter the number of hours (0-24):'))
    minutes = int(input('enter the number of minutes (0-60):'))
    seconds = int(input('enter the number of seconds (0-60):'))
    time.sleep((hours*60*60)+(minutes*60)+seconds)
    print('Time up')
    playsound('Alarm-Fast-A1-www.fesliyanstudios.com.mp3')
else:
    create_permission = input('do you want to create a custom time:')
    if create_permission == 'yes':
        create_custom = input('name of your custom time:')
        custom_hours = input('enter the number of hours (0-24):')
        custom_minutes = input('enter the number of minutes (0-60):')
        custom_seconds = input('enter the number of seconds (0-60):')
        if len(custom_seconds) == 1:
            custom_seconds = '0'+'0'+custom_seconds
        if len(custom_seconds) == 2:
            custom_seconds = '0' + custom_seconds
        if len(custom_minutes) == 1:
            custom_minutes = '0'+'0'+custom_minutes
        if len(custom_minutes) == 2:
            custom_minutes = '0' + custom_minutes

        custom_dict = {}

        with open('custom-timer-database.txt','a') as f:
            f.write(f'{create_custom}:{custom_hours+custom_minutes+custom_seconds}\n')
    else:
        custom_dict = {}
        with open('custom-timer-database.txt','r') as f:
            a = f.readlines()
            for i in a:
                time_data = list(i.split('\n')[0].split(':')[1])
                seconds = int(time_data[len(time_data)-3]+time_data[len(time_data)-2]+time_data[len(time_data)-1])
                time_data.pop(len(time_data)-1)
                time_data.pop(len(time_data)-1)
                time_data.pop(len(time_data)-1)
                minutes = int(time_data[len(time_data)-3]+time_data[len(time_data)-2]+time_data[len(time_data)-1])
                time_data.pop(len(time_data)-1)
                time_data.pop(len(time_data)-1)
                time_data.pop(len(time_data)-1)
                hours = ''
                for j in time_data:
                    hours = hours + j
                custom_dict[i.split('\n')[0].split(':')[0]] = [int(hours),minutes,seconds]
        timer_name = input('name of your custom time:')
        time.sleep((custom_dict[timer_name][0]*60*60)+(custom_dict[timer_name][1]*60)+custom_dict[timer_name][2])
        print('Time up')