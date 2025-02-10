import sqlite3
import tkinter
from tkinter import *
from tkinter.ttk import Notebook

import pandas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class MainWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Computer RMM Visual")
        self.geometry("460x320")
        self.notebook = Notebook(self)
        #self.notebook.grid(row=0,column=10,columnspan=2,sticky="nsew")
        self.notebook.pack()

#       Building the needed Frames
        options_given = ["About","Vendors","Manufacturer","Operating Systems"]

        f1 = self.newFrame(self.notebook,title=options_given[0])
        f2 = self.newFrame(self.notebook,title=options_given[1])
        f3 = self.newFrame(self.notebook,title=options_given[2])
        f4 = self.newFrame(self.notebook,title=options_given[3])

#       Setting up frame1 or "f1"
        Label(f1,text="This is the default page to start at.").pack()
        Label(f1,text="This app made and re-built by Aaron Ogle").pack()
        Label(f1,text="This is a way of showing a dataset using tkinter.").pack()

#       Setting up frame2 or "f2"

#       Setting up frame3 or "f3"

#       Setting up frame4 or "f4"


#       A reusable Frame, this is used with a notebook.
#       There only really needs to be one for this project.
    def newFrame(self, notebook, title):
        frame = Frame(notebook)
        notebook.add(frame, text=title)
        return frame  # This returns a frame object

    def newFigure(self):
        pass

    def baseQuery(self,query):
        connection = sqlite3.connect("main.db")
        df = pandas.read_sql(query,connection)
        connection.close()
        return df

App = MainWindow()
App.mainloop()
