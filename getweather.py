# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:13:43 2019

@author: Alicja
"""

import tkinter as tk
import requests
HEIGHT = 700
WIDTH = 800

#API key
#f1c009808bbe50b7f3ab786ff1ac1205
#url
#api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature: %s' % (name, desc, temp)
    except:
        final_str = 'There was a problem retrieving that information'
        
    return final_str
def get_weather(city):
    weather_key = "f1c009808bbe50b7f3ab786ff1ac1205"
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {'APPID' : weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params = params)
    weather = response.json()
    
    label['text'] = format_response(weather)
    

root = tk.Tk() #root window

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file = 'landscape.png')
backgroud_label = tk.Label(root, image = background_image)
backgroud_label.place(relwidth =1, relheight = 1)

frame = tk.Frame(root, bg = '#80c1ff', bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n') #1-wypełnia cały ekran, można dać mniej

entry = tk.Entry(frame, font = ('Courier', 18))
entry.place(relwidth = 0.65, relheight = 1)

button = tk.Button(frame, text = "Get Weather", bg = 'gray', font = ('Courier', 12), command = lambda: get_weather(entry.get()))

button.place(relx = 0.7, rely = 0, relwidth = 0.3, relheight = 1)

lower_frame = tk.Frame(root, bg = '#80c1ff', bd =10)
lower_frame.place(anchor = 'n', relx = 0.5, rely  = 0.25, relwidth = 0.75, relheight = 0.6)                       

label = tk.Label(lower_frame,  bg = 'white', font = ('Courier', 18), anchor = 'nw', justify = 'left', bd =4)
label.place(relwidth = 1, relheight = 1)

root.mainloop()