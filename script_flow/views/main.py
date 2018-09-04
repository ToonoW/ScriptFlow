# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import Button

from script_flow.models import MainConponentModel


class MainView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # self.pack()

        self.create_func_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def create_func_widgets(self):
        conponents = MainConponentModel.objects().all()
        for index, conp in enumerate(conponents):
            Button(self.master, text=conp.title).grid(
                row=index//2, column=index % 2)

    def say_hi(self):
        print("hi there, everyone!")
