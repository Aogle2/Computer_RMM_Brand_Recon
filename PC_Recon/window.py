'''

The primary notebook is going to have another notebook in Tab 2 named (Statistics) which wil have async functions and each will have a refresh button for each.
Primary Notebook will be "About" and Another will be "Statistics"

The Primary Notebook will have Two Sub-Notebooks

---About - The default tab to go to when program is started.
    |
    -----System Info, With export csv/excel Button (Asynced)
    |
    -----Database Info, With export csv/excel Button (Asynced)
    |
    ----About Author, With export csv/excel Button (Asynced)

---Statistics
    |
    ----Vendor Count (view), with Refresh Button and export csv/excel button
    |
    ----Manufacture (view), with Refresh Button and export csv/excel button
    |
    ----Operating System Count (view), with Refresh Button and export csv/excel button

--Settings
    |
    ----System Settings
        |Will have Save location for any current settings
        |Will have settings for Style and stuff for the windows
        |Will have an export and import settings as well.

    ----Database Settings
        |TBA
-----------------------------------------------------------------------------------------

About will have System info and Database Info as well as Something about the program author.

Statistics will be a summary of the other views, after they've been re-written and some of the names changed.

Each tab will be identified and refreshed based on that info alone.

This is a pipe dream below
I also want to work in a feadback system to the DB (computer info, run time, any errors, error count and how many times something was clicked)
'''
from  tkinter import *
from tkinter.ttk import *


#The thing to keep this from running right off the bat..
if __name__ == "__main__":
    pass
