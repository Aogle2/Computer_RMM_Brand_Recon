'''
This revision is going to add

1. Lazy loading for each tab.
2. Correct font loading and font size for each platform.
3. themes
4. External DB May use this module: https://docs.devart.com/python/mysql/connect-python-apps-using-ssh.htm

Modules Needed overall (WIP)
1. Matplotlib
    A. Display our charts.

2. Tkinter
    A. Display stuff

3. devart-mysql-connector
    A. Connect to the MySQL server remotely using SSH

4. OS
    A. Gather Basic Info regarding the computer running this.
5. sys
    A. Gather more basic info regarding the computer running this.
6. Platform
    A. Gather Even more basic data about the computer.


Features I want to add
1. Welcome screen, introducing me or something.
    A. Buttons to show Info about computer stuff and program info
2. Charts and Data screen
    A. Selectable Charts with Selectable Data via drop down selections.

'''


#Class that has the core tkinter module

import tkinter as tk
from tkinter.ttk import Notebook, Frame, Radiobutton


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RMM Metric")
        self.geometry("800x600")

    # Make the notebook, this is generic for the entire program, and we only need one so far.
        self.notebook = Notebook(self)


#   Method for checking what radio button is clicked.

#   Method for checking what drop down is selected.

#   Dynamic radio buttons using pack https://www.pythontutorial.net/tkinter/tkinter-radio-button/, another cool one: https://ultrapythonic.com/tkinter-radiobutton/

#   Method to make the dropdown. https://pythonassets.com/posts/drop-down-list-combobox-in-tk-tkinter/

#   Method to make a Frame
    def newFrame(self, notebook, title):
        #Create our frame object and assign it to the notebook.
        frame = Frame(notebook)
        notebook.add(frame, text = title)
        return frame

#   Method to make the Bar Chart

#   Method to make a Histogram

#   Method to make a Pie Chart

#   Method to handle events : https://stackoverflow.com/questions/32289175/list-of-all-tkinter-events
'''
https://pythonexamples.org/python-tkinter-radiobutton-check-if-an-option-is-selected/

'''


if __name__ == '__main__':
    Window = App()
    Window.mainloop()