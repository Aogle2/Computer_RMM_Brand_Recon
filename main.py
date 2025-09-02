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

from tkinter import *
from tkinter.ttk import Notebook, Frame, Radiobutton


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("RMM Metrics")
        self.geometry("800x600")

#   Method for checking what radio button is clicked.

#   Dynamic radio buttons using pack https://www.pythontutorial.net/tkinter/tkinter-radio-button/, another cool one: https://ultrapythonic.com/tkinter-radiobutton/
        self.radioButton1 = Radiobutton(self, text="Computers")
        self.radioButton1.grid(row=0, column=0)

#   Method to make the dropdown. https://pythonassets.com/posts/drop-down-list-combobox-in-tk-tkinter/

#   Method to make the Bar Chart

#   Method to make a Histogram

#   Method to make a Pie Chart

#   Method to do the query and return a dictionary

#   Method to handle events : https://stackoverflow.com/questions/32289175/list-of-all-tkinter-events
'''
https://pythonexamples.org/python-tkinter-radiobutton-check-if-an-option-is-selected/

'''


'''
Create classes for each element and widget that is needing to be used.
Will also use a lot of: https://www.geeksforgeeks.org/python/multiple-inheritance-in-python/
May also need to use: https://www.geeksforgeeks.org/python/data-abstraction-in-python/

Create a Notebook
Create a Frame
Create a Button
Create a Radiobutton


Class to Monitor Events
https://pythonguides.com/python-tkinter-events/




'''

if __name__ == '__main__':
    Window = App()
    Window.mainloop()


