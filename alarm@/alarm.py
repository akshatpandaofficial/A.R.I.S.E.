import datetime
import time
import os
from playsound import playsound
os.chdir('C://Users//AkshatPanda//Desktop//A.R.I.S.E//alarm')
create_permission = input('do you want to create an alarm ?:')
if create_permission == 'yes':
    while True:
        create_custom = input('enter name of alarm:')
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

        with open('custom-alarm-database.txt','a') as f:
            f.write(f'{create_custom}:{custom_hours+custom_minutes+custom_seconds}\n')
        

        monday_repeat = input('do you want to repeat on monday ?(0 or 1):')
        tuesday_repeat = input('do you want to repeat on tuesday ?(0 or 1):')
        wednesday_repeat = input('do you want to repeat on wednesday ?(0 or 1):')
        thursday_repeat = input('do you want to repeat on thursday ?(0 or 1):')
        friday_repeat = input('do you want to repeat on friday ?(0 or 1):')
        saturday_repeat = input('do you want to repeat on saturday ?(0 or 1):')
        sunday_repeat = input('do you want to repeat on sunday ?(0 or 1):')

        with open('custom-alarm-repeat-database.txt','a') as f:
            f.write(f'{create_custom}:{monday_repeat + tuesday_repeat + wednesday_repeat + thursday_repeat + friday_repeat + saturday_repeat + sunday_repeat}\n')
        
        leave = input("are you done ?:")
        if leave == 'yes':
            break
        else:
            pass

with open('custom-alarm-database.txt','r') as f:
    a = f.readlines()
    custom_dict = {}
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
        int_hours = int(hours)
        custom_dict[i.split('\n')[0].split(':')[0]] = [int_hours,minutes,seconds]
    

with open('custom-alarm-repeat-database.txt','r') as g:
    b = g.readlines()
    repeat_dict = {}
    for i in b:
        repeat_data = list(i.split('\n')[0].split(':')[1])
        temp_list = []
        week_list = list(range(0,7))
        for j in repeat_data:
            for k in week_list:
                temp_list.append([k,j])
                week_list.remove(k)
                break
        repeat_dict[i.split('\n')[0].split(':')[0]] =  temp_list



run_permission = input('do you want to run the alarm application ?:')
if run_permission == 'yes':
    while True:
        for i in repeat_dict:
            for j in repeat_dict[i]:
                if j[0] == time.gmtime().tm_wday and j[1] == '1':
                    if custom_dict[i][0] == datetime.datetime.now().hour and custom_dict[i][1] == datetime.datetime.now().minute and custom_dict[i][2] == datetime.datetime.now().second:
                        while custom_dict[i][0] == datetime.datetime.now().hour and custom_dict[i][1] == datetime.datetime.now().minute and datetime.datetime.now().second < 59:
                            playsound('Alarm-Fast-A1-www.fesliyanstudios.com.mp3')