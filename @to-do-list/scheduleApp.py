import datetime
import os
import time

import playsound


def run():
    with open('schedule-time-database.txt','r') as f:
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
            time_dict[i.split('\n')[0].split(':')[0]] = [int(hours),minutes,seconds]
    with open('schedule-repeat-database.txt','r') as g:
        b = g.readlines()
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
    with open('schedule-description-database.txt','r') as f:
        description_list = f.readlines()
        for i in a:
            description_data = i.split('\n')[0].split(':')[1]
            description_dict[i.split('\n')[0].split(':')[0]] = description_data
    with open('schedule-duration-database.txt','r') as f:
        duration_list = f.readlines()
        for i in duration_list:
            duration_data = list(i.split('\n')[0].split(':')[1])
            seconds = int(duration_data[len(duration_data)-3]+duration_data[len(duration_data)-2]+duration_data[len(duration_data)-1])
            duration_data.pop(len(duration_data)-1)
            duration_data.pop(len(duration_data)-1)
            duration_data.pop(len(duration_data)-1)
            minutes = int(duration_data[len(duration_data)-3]+duration_data[len(duration_data)-2]+duration_data[len(duration_data)-1])
            duration_data.pop(len(duration_data)-1)
            duration_data.pop(len(duration_data)-1)
            duration_data.pop(len(duration_data)-1)
            hours = ''
            for j in duration_data:
                hours = hours + j
            duration_dict[i.split('\n')[0].split(':')[0]] = [int(hours),minutes,seconds]
    print(time_dict)
    print(repeat_dict)
    print(description_dict)
    print(duration_dict)


def createfunc():
    task_name = input('name of your task:')
    custom_hours = input('enter the hours number (0-24):')
    custom_minutes = input('enter the minutes number (0-60):')
    custom_seconds = input('enter the seconds number (0-60):')
    task_description = input('describe the task:')
    period_hours = input('enter number of hours for task:')
    period_minutes = input('enter number of minutes for task:')
    period_seconds = input('enter number of seconds for task:')

    monday_repeat = input('do you want to repeat on monday ?(0 or 1):')
    tuesday_repeat = input('do you want to repeat on tuesday ?(0 or 1):')
    wednesday_repeat = input('do you want to repeat on wednesday ?(0 or 1):')
    thursday_repeat = input('do you want to repeat on thursday ?(0 or 1):')
    friday_repeat = input('do you want to repeat on friday ?(0 or 1):')
    saturday_repeat = input('do you want to repeat on saturday ?(0 or 1):')
    sunday_repeat = input('do you want to repeat on sunday ?(0 or 1):')
    if len(custom_seconds) == 1:
        custom_seconds = '0'+'0'+custom_seconds
    if len(custom_seconds) == 2:
        custom_seconds = '0' + custom_seconds
    if len(custom_minutes) == 1:
        custom_minutes = '0'+'0'+custom_minutes
    if len(custom_minutes) == 2:
        custom_minutes = '0' + custom_minutes
    if len(period_seconds) == 1:
        period_seconds = '0'+'0'+period_seconds
    if len(period_seconds) == 2:
        period_seconds = '0' + period_seconds
    if len(period_minutes) == 1:
        period_minutes = '0'+'0'+period_minutes
    if len(period_minutes) == 2:
        period_minutes = '0' + period_minutes
    if os.path.isfile('schedule-time-database.txt')==True and os.path.isfile('schedule-duration-database.txt')==True:
        def warningfunc():
            run()
            input_repeat = [monday_repeat, tuesday_repeat, wednesday_repeat, thursday_repeat, friday_repeat, saturday_repeat, sunday_repeat]
            check_repeat = {}
            for i in repeat_dict:
                check_repeat[i] = []
                for j in repeat_dict[i]:
                    for k in input_repeat:
                        if j[1] == k and j[1] == '1':
                            check_repeat[i].append([j[0], j[1]])
                            break
            print(check_repeat)
            input_time = [int(custom_hours) * 60 * 60 + int(custom_minutes) * 60 + int(custom_seconds), (int(custom_hours) + int(period_hours)) * 60 * 60 + (int(custom_minutes) + int(period_minutes)) * 60 + int(custom_seconds) + int(period_seconds)]
            new_time_dict = {}
            for i in time_dict:
                new_time_dict[i] = [time_dict[i][0] * 60 * 60 + time_dict[i][1] * 60 + time_dict[i][2],(time_dict[i][0] + duration_dict[i][0]) * 60 * 60 + (time_dict[i][1] + duration_dict[i][1]) * 60 + (time_dict[i][2] + duration_dict[i][2])]
            for i in new_time_dict:
                for j in range(0,len(check_repeat[i])):
                    check_time = (input_time[1] in range(new_time_dict[i][0], new_time_dict[i][1] + 1)) or (input_time[0] in range(new_time_dict[i][0], new_time_dict[i][1] + 1))
                    if check_time:
                        print(f'{task_name} overlaps {i} on day {check_repeat[i][j][0]}.')
                        overlap_override = input('are you sure about overlap:')
                        if overlap_override == 'yes':
                            pass
                        else:
                            createfunc()
        warningfunc()
    with open('schedule-time-database.txt','a') as f:
        f.write(f'{task_name}:{custom_hours+custom_minutes+custom_seconds}\n')
    with open('schedule-description-database.txt','a') as f:
        f.write(f'{task_name}:{task_description}\n')
    with open('schedule-repeat-database.txt','a') as f:
        f.write(f'{task_name}:{monday_repeat + tuesday_repeat + wednesday_repeat + thursday_repeat + friday_repeat + saturday_repeat + sunday_repeat}\n')
    with open('schedule-duration-database.txt','a') as f:
        f.write(f'{task_name}:{period_hours+period_minutes+period_seconds}\n')


def changefunc():
    run()
    print()
    print("time-dictionary",time_dict)
    print()
    print("repeat-dictionary",repeat_dict)
    change_name = input('enter name of task to be edited:')
    with open('schedule-time-database.txt','r') as f:
        mylist = f.readlines()
    for i in range(len(mylist)):
        if mylist[i].split('\n')[0].split(':')[0] == change_name:
            change_hour = input("enter hour number:")
            change_min = input('enter minute number:')
            change_sec = input('enter second number:')
            if len(change_sec) == 1:
                change_sec = '0'+'0'+change_sec
            if len(change_sec) == 2:
                change_sec = '0' + change_sec
            if len(change_min) == 1:
                change_min = '0'+'0'+change_min
            if len(change_min) == 2:
                change_min = '0' + change_min
            mylist[i] = change_name+':'+change_hour+change_min+change_sec+'\n'
    with open('schedule-repeat-database.txt','r') as f:
        repeat_list = f.readlines()
    for i in range(len(repeat_list)):
        if repeat_list[i].split('n')[0].split(':')[0] == change_name:
            change_monday_repeat = input('do you want to repeat on monday ?(0 or 1):')
            change_tuesday_repeat = input('do you want to repeat on tuesday ?(0 or 1):')
            change_wednesday_repeat = input('do you want to repeat on wednesday ?(0 or 1):')
            change_thursday_repeat = input('do you want to repeat on thursday ?(0 or 1):')
            change_friday_repeat = input('do you want to repeat on friday ?(0 or 1):')
            change_saturday_repeat = input('do you want to repeat on saturday ?(0 or 1):')
            change_sunday_repeat = input('do you want to repeat on sunday ?(0 or 1):')
            repeat_list[i] = change_name+':'+change_monday_repeat+change_tuesday_repeat+change_wednesday_repeat+change_thursday_repeat+change_friday_repeat+change_saturday_repeat+change_sunday_repeat+'\n'
    with open('schedule-repeat-database.txt','w') as f:
        f.writelines(repeat_list)
    with open('schedule-time-database.txt','w') as f:
        f.writelines(mylist)

def deletefunc():
    delete_name = input('enter name of task to be deleted:')
    with open('schedule-time-database.txt','r') as f:
        mylist = f.readlines()
    for i in range(len(mylist)):
        if mylist[i].split('\n')[0].split(':')[0] == delete_name:
            mylist.pop(i)
    with open('schedule-time-database.txt','w') as f:
        f.writelines(mylist)

os.chdir('/@to-do-list')

time_dict = {}
description_dict = {}
repeat_dict = {}
duration_dict = {}

while True:
    command = input('create or delete or change or run or quit (choose any one):')
    if command == 'create':
        createfunc()
    elif command == 'delete':
        deletefunc()
    elif command == 'change':
        changefunc()
    elif command == 'run':
        run()
        for i in repeat_dict:
            for j in repeat_dict[i]:
                for k in time_dict:
                    if time.localtime(time.time()).tm_wday == j[0] and j[1] == '1':
                        if time.localtime(time.time()).tm_hour == time_dict[i][0] and time.localtime(time.time()).tm_min == time_dict[i][1] and time.localtime(time.time()).tm_sec == time_dict[i][2]:
                            playsound('Alarm-Fast-A1-www.fesliyanstudios.com.mp3')
    elif command == 'quit':
        break