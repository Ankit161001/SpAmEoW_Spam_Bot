# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 00:25:41 2021

Source code for SpAmEoW ver 1.01

@author: Ankit Rana
"""

import tkinter as tk
import pyautogui as pa
import time


class SampleApp(tk.Tk):
    def spam_1(self):
        print("hello")
        
    def spam_main(self):
        self.message = self.entry1.get()
        self.rep = self.entry2.get()

        try:
            rep2 = float(self.rep)
            reps = int(rep2)
        except:
            reps = 5
        length = len(self.message)
        time.sleep(10)
        for i in range(0,reps):
            for j in range(0,length):
                if(self.message[j]==" "):
                    pa.press("enter")
                pa.press(self.message[j])
            pa.press("enter")
            
  
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("400x400")
        self.title("SpAmEoW")
                
        self.bg = tk.PhotoImage(file = "spam_meow.png")
            # Show image using label
        self.label1 = tk.Label( self, image = self.bg)
        self.label1.place(x = 0, y = 0)
        
        self.label2 = tk.Label(self, text = "Spam Responsibly!!", fg="white", bg="#ff81d0")
        self.label2.place(x=20, y=20)
        
        self.label3 = tk.Label(self, text = "Enter Text", fg="white", bg="#ff81d0")
        self.label3.place(x=20, y=50)
        
        self.entry1 = tk.Entry(self, width="20")
        self.entry1.place(x=160, y=50)
        
        self.label4 = tk.Label(self, text = "Enter Repetitions", fg="white", bg="#ff81d0")
        self.label4.place(x=20, y=80)
        
        self.entry2 = tk.Entry(self, width="20")
        self.entry2.place(x=160, y=80)
        
        self.button1 = tk.Button(self, text = "SPAM", fg="white", bg="#ff81d0", command = self.spam_main )
        self.button1.place(x=30, y=150)


app = SampleApp()
app.mainloop()