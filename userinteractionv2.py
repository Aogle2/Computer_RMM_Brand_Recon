import platform
import sqlite3
import tkinter
from tkinter import *
from tkinter.ttk import Notebook

import pandas
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class MainWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Computer RMM Visual")
        self.geometry("460x420")
        self.resizable(height=False,width=False)
        self.notebook = Notebook(self)
        #self.notebook.grid(row=0,column=10,columnspan=2,sticky="nsew")
        self.eval('tk::PlaceWindow . center')

        #This puts this in teh middle of the window
        self.notebook.pack()

#       Building the needed Frames
        options_given = ["About","Vendors","Manufacturer","Operating Systems"]

        self.f1 = self.newFrame(self.notebook,title=options_given[0])
        self.f2 = self.newFrame(self.notebook,title=options_given[1])
        self.f3 = self.newFrame(self.notebook,title=options_given[2])
        self.f4 = self.newFrame(self.notebook,title=options_given[3])

#       Setting up frame1 or "f1"
        Label(self.f1,text="This is the default page to start at.").pack()
        Label(self.f1,text="This app made and re-built by Aaron Ogle").pack()
        Label(self.f1,text="This is a way of showing a dataset using tkinter.").pack()
        Label(self.f1,text="").pack()
        Label(self.f1,text=f"OS: {platform.platform()}").pack()
        Label(self.f1,text=f"Processor: {platform.processor()}").pack()

#       Setting up frame2 or "f2"
        #Maybe this can be a sub method in a sub method.
        fig, ax = plt.subplots()
        ax.bar(x=['A','B','C','D'],
               height=[10,20,15,25],
               color=['blue','green','red','purple'])

        ax.set_title("Same Graph")
        ax.set_xlabel('Catagory')
        ax.set_ylabel('Value')
        canvas = FigureCanvasTkAgg(fig,master=self.f2)
        canvas.draw()
        canvas.get_tk_widget().pack()

#       Setting up frame3 or "f3"

#       Setting up frame4 or "f4"



#       A reusable Frame, this is used with a notebook.
#       There only really needs to be one for this project.
    def newFrame(self, notebook, title):
        frame = Frame(notebook)
        notebook.add(frame, text=title)
        return frame  # This returns a frame object

    def baseQuery(self,query):
        connection = sqlite3.connect("main.db")
        df = pandas.read_sql(query,connection)
        connection.close()
        return df

    def newPlot(self,title,xlabel,ylabel,**data):
        fig, ax = plt.subplots()
        #Work on randomizing colors.
        ax.bar(x=pd.Series(list(data.keys())),
               height=pd.Series(list(data.values())),
               color=['blue', 'green', 'red', 'purple'])

        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack()




App = MainWindow()
App.mainloop()