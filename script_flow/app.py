import tkinter as tk

from script_flow.views.main import MainView
from script_flow import models


mainview = models.MainViewModel(VIEWS['MainView'])

root = tk.Tk()
root.title(mainview.title)
root.geometry(mainview.geometry)

app = MainView(master=root)
