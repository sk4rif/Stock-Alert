# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 21:18:39 2020

@author: Lenovo
"""
from yahoo_fin import stock_info as si
from pygame import mixer
import tkinter as tk
import pandas as pd
pd.options.mode.chained_assignment = None
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 300, height = 300) # create the canvas
canvas1.pack()
entry1 = tk.Entry (root) # create the entry box
entry2 = tk.Entry (root)
canvas1.create_window(150, 50, window=entry1)
canvas1.create_window(150, 210, window=entry2)
def insert_number(): # add a function/command to be called by the button (i.e., button1 below)
    global x1 # add 'global' before the variable x1, so that you can use that variable outside of the command/function if ever needed
    global x2
    x1 = str(entry1.get()) # store the data input by the user as a variable x1 
    x2 = str(entry2.get())
button1 = tk.Button (root, text='Input stock Ticker (XXXX) ',command=insert_number, bg='blue', fg='white') # button to call the 'inserter' command above 
button2 = tk.Button (root, text='Stock level', command=insert_number, bg='green', fg='white')
canvas1.create_window(150, 80, window=button1)
canvas1.create_window(150, 240, window=button2)
root.mainloop()
mixer.init()
mixer.music.load("alert.mp3.mp3")
while 650 < si.get_live_price(f'{x1}') <= 1600:
    if si.get_live_price(f'{x1}') == 2:
        continue
    print(si.get_live_price(f'{x1}'))
print('Stock Alert, Level Hit.')
mixer.music.play()