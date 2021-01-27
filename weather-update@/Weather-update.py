import os
from bs4 import BeautifulSoup
import requests
os.chdir('C://Users//AkshatPanda//Desktop//A.R.I.S.E//weather-update@')
'''location'''
r = requests.get('https://www.eldoradoweather.com/forecast/india/Bhubaneswar/Bhubaneswar.php')
html = BeautifulSoup(r.content,'html.parser')
location_list = html.find_all('span',style='font-family:arial; color:#000000; font-size:15px; font-weight:bold;')
for location in location_list:
    a = location.get_text().split(' ')
    if a[len(a)-1] == 'IN':
        a[len(a)-1] = 'India'
location_result1 = ''
for i in a:
    location_result1 = location_result1 + i
location_list1 = location_result1.split('\n')
location_list1.remove(location_list1[0])
print()
print('location is '+location_list1[0]+'.')
print()
'''humidity'''
humidity = html.find_all('td',style='margin-top:4px;')
for i in humidity[1].find_all('span',style='font-family:ubuntu; color:#008000; font-size:15px;'):
    humidity_result = 'humidity is'+i.get_text().split('\n')[1].split('%')[0]+'percent.'
'''temperature'''
for i in humidity[2].find_all('span',style='color:#000000;'):
    for j in i.get_text().split('\n'):
        temp_result = f'temperature is {j}.'
print(temp_result)
print()
'''wind'''
wind_list = html.find_all('td',style="width:280px; padding-right:4px; margin-top:4px;")
for i in wind_list:
    wind_list1 = i.find_all('span',style="color:#000000;")
for j in wind_list1:
    c = list(j.get_text())
    for k in range(len(c)-1):
        if c[k] == '\xa0':
            c.remove('\xa0')
        if c[k] == 'N':
            c[k] = 'North '
        if c[k] == 'S':
            c[k] = 'South '
        if c[k] == 'E':
            c[k] = 'East '
        if c[k] == 'W':
            c[k] = 'West '
        if c[k] == 'k':
            c[k] = 'km'
wind_result = ''
for i in c:
    wind_result = wind_result + i
print(f'wind is {wind_result}.')
print()
'''visibility'''
visibility_list = html.find_all('td',style="padding-right:4px; margin-top:4px;")
print('visibility is',visibility_list[1].find_all('span',style="color:#000000;")[0].get_text()+'.')
print()
'''sunrise'''
sunrise_list = list(html.find_all('td',style="width:250px; padding-bottom:0px; margin-top:4px;")[0].find_all('span')[0].get_text())
sunrise_time = ''
for i in sunrise_list:
    if i == '\n':
        sunrise_list.remove('\n')
for i in range(len(sunrise_list)):
    if sunrise_list[i] == ':':
        sunrise_list[i] = ' hours '
    if sunrise_list[i] == ' ':
        sunrise_list[i] = ' minutes '
for i in sunrise_list:
    sunrise_time = sunrise_time + i
print('sunrise at',sunrise_time+'.')
print()
'''sunset'''
sunset_list = list(html.find_all('td',style="width:250px; padding-bottom:6px; margin-top:0px;")[0].find('span').get_text())
sunset_time = ''
for i in sunset_list:
    if i == '\n':
        sunset_list.remove('\n')
for i in range(len(sunset_list)):
    if sunset_list[i] == ':':
        sunset_list[i] = ' hours '
    if sunset_list[i] == ' ':
        sunset_list[i] = ' minutes '
for i in sunset_list:
    sunset_time = sunset_time + i
print('sunset at',sunset_time+'.')

with open('weather-update.txt','w') as f:
    f.write('location is '+location_list1[0]+'.\n')
    f.write(humidity_result+'\n')
    f.write(temp_result+'\n')
    f.write(f'wind is {wind_result}.')
    f.write('visibility is'+visibility_list[1].find_all('span',style="color:#000000;")[0].get_text()+'.'+'\n')
    f.write('sunrise at '+sunrise_time+'.'+'\n')
    f.write('sunset at '+sunset_time+'.'+'\n')