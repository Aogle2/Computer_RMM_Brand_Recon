'''
This one is going to be factoring in asyncio and type hinting.
The first page is going to have a summary of the computer it is running on (notebook 1, Tab 1)  with another subnotebook with two tabs)
It's also going to have a summary of the database that is used, how many rows, the size of it and creation date. Notebook 1 (Tab 2)

Modules that are going to be used for this project revamp
DLT - Data Load Tool, this is going to talk to the DB.
MatPlotlib - used to plot our data.
Pandas - I am going to try to not use this as much but this is used to get our data in a usable sense for matplotlib.


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
-----------------------------------------------------------------------------------------
Need to re-design the Database as well for this.

Tables that are needed
    Table---endpoint
        |----id
        |----serial_number
        |----

    Table---vendor
        |----id
        |----name
        |----type


    Table---software_vendor
    PK  |----id
        |----name
        |----license_type
        |----

    Table---machine_manufacturer
        |----id

    Table---operating_system
    PK  |----id
        |----os_friendly_name
        |----os_build_num
    FK  |----os_vendor_id
        |----os_arch

    Table---feedback
        |----id
        |----os_id_fk
        |----run_time
        |----last_error
        |----leap_year
        |----python_ver



-----------------------------------------------------------------------------------------

About will have System info and Database Info as well as Something about the program author.

Statistics will be a summary of the other views, after they've been re-written and some of the names changed.

Each tab will be identified and refreshed based on that info alone.

This is a pipe dream below
I also want to work in a feadback system to the DB (computer info, run time, any errors, error count and how many times something was clicked)
'''
from tkinter import *


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title = "Test"


    #Going to port over some of the repeatable methods from the other projects.
    #Going to create a primary Notebook and then a nested notebook.
    #The goal is to use reuseable methods for this


#The methods used for this project






App = MainWindow()
App.mainloop()