"""
This is going ot be used for the UI and other front end items.
This is going to be linked to the DB


Look into: https://realpython.com/python-gui-with-wxpython/
Another look into: https://wiki.wxpython.org/How%20to%20Learn%20wxPython

MacOS has some more setup from what I've read, I am going to look into this a little bit later.
Running this on "MacOS Tahoe", M1 Max Macbook Pro



Ubuntu requires a bit more pre-work before it can work, maybe look into how all this can be pakaged in one go for a client?
Ubuntu will require a bit more work as it needs GTK+ installed along with some other stuff.
"""
import os
import platform

import wx
"""

import wx
# Just some basic hello world thing.

app = wx.App()

frame = wx.Frame(None, title="Hello world!")

frame.Show(True)
app.MainLoop()
"""
import wx
import psutil

class Tab(wx.Panel):
    def __init__(self, parent, label):
        super().__init__(parent)

        sizer = wx.BoxSizer(wx.VERTICAL)

        text = wx.StaticText(self, label=label)
        sizer.Add(text, 0, wx.ALL | wx.CENTER, 10)

        self.SetSizer(sizer)


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="WxTest", size=(400, 300))

        # Notebook (tab container)
        notebook = wx.Notebook(self)

        menubar = wx.MenuBar()
        filemenu = wx.Menu()

        filemenu.Append(wx.ID_ANY, "&File", "&Open a file")
        filemenu.AppendSeparator()
        exitoption = filemenu.Append(wx.ID_ANY, "&Exit", "&Exit")

        scaled = wx.Image("x.png",wx.BITMAP_TYPE_ANY).Scale(16,16,wx.IMAGE_QUALITY_HIGH)


        exitoption.SetBitmap(wx.Bitmap(scaled))
        self.Bind(wx.EVT_MENU,self.on_quit_program,id=exitoption.GetId())

        menubar.Append(filemenu,'File')

        options = wx.Menu()
        options.AppendCheckItem(wx.ID_ANY,'Settings')
        options.AppendCheckItem(wx.ID_ANY,'Appearance')



        menubar.Append(options, 'Options')

        self.SetMenuBar(menubar)

        # Create tabs
        tab1 = Tab(notebook, "Tab 1")
        tab2 = Tab(notebook, "Tab 2")
        tab3 = Tab(notebook, "Tab 3")
        tab4 = Tab(notebook, '')

        self.label = wx.StaticText(tab3,label="Starting up...", pos=(20,20))

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER,self.on_update,self.timer)
        self.timer.Start(100)

        # Buttons
        button1 = wx.Button(tab1, label="Button 1")
        button2 = wx.Button(tab2, label="Button 2", pos=(1, 2))

        self.rb1 = wx.RadioButton(tab1, label="Radio Button 1")
        self.rb2 = wx.RadioButton(tab1, label="Radio Button 2")
        self.rb3 = wx.RadioButton(tab1, label="Radio Button 3")

    # This is what makes that little box thing that you see in old Windows Task Manager.
        self.rbox1 = wx.RadioBox(tab2, label="Radio Box Thing 1", choices=["Option 1", "Option 2", platform.machine()], majorDimension=1,style=wx.RA_SPECIFY_COLS)


        """
        Create our Info box thing and the parent that is going to house this is "Tab4", which their parent is the notebook.
        info_box = wx.StaticBox(tab4, label="System Information")
        
        This is our container itself, vertical means that this will arrange things vertically 
        info_sizer = wx.StaticBoxSizer(info_box, wx.VERTICAL)

        These are our controls or  content to the container to the container
        label1 = wx.StaticText(tab4, label="Hostname: server01")
        label2 = wx.StaticText(tab4, label="CPU: Intel Xeon")
        label3 = wx.StaticText(tab4, label="RAM: 64 GB")

        info_sizer.Add(label1, 0, wx.ALL, 5)
        info_sizer.Add(label2, 0, wx.ALL, 5)
        info_sizer.Add(label3, 0, wx.ALL, 5)

        
        """


        infoBox = wx.StaticBox(tab4, label="System Information")
        info_sizer = wx.StaticBoxSizer(infoBox,wx.VERTICAL)


        hostname = wx.StaticText(tab4,label=f"Hostname: {platform.node()}")
        memory = wx.StaticText(tab4,label=f"Memory: {psutil.virtual_memory().percent}%")

        info_sizer.Add(hostname, 0, wx.ALL | wx.CENTER, 10)
        info_sizer.Add(memory, 0, wx.CENTER, 10)


        # Add button to tab1's sizer
        tab1.GetSizer().Add(button1, 0, wx.ALL | wx.CENTER, 10)

        # Bind event
        button1.Bind(wx.EVT_BUTTON, self.button_on_click)

        tab1.GetSizer().Add(self.rb1, 0, wx.ALL | wx.LEFT, 10)
        tab1.GetSizer().Add(self.rb2, 0, wx.ALL | wx.LEFT, 10)
        tab1.GetSizer().Add(self.rb3, 0, wx.ALL | wx.LEFT, 10)
        tab2.GetSizer().Add(self.rbox1, 2, wx.ALL | wx.CENTER, 15)
        tab4.GetSizer().Add(info_sizer, 0, wx.ALL | wx.EXPAND, 10)




        # Add tabs to notebook
        notebook.AddPage(tab1, "Tab 1")
        notebook.AddPage(tab2, "Tab 2")
        notebook.AddPage(tab3, "Tab 3")
        notebook.AddPage(tab4, "System Information")





        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.EXPAND)


        self.SetSizer(sizer)

        self.Centre()
        self.Show()

    def on_quit_program(self,event):
        self.Close(True)

    def on_update(self,event):
        self.label.SetLabel(f"{self.get_current_memory():2f}")


    def get_current_memory(self):
        return psutil.Process(os.getpid()).memory_info().rss

    def button_on_click(self, event):
        result = wx.MessageBox(
            f"Do you want to continue?",
            "Question",
            wx.YES_NO | wx.ICON_QUESTION
        )

        if result == wx.YES:
            print("User clicked YES")
        else:
            print("User clicked NO")


if __name__ == '__main__':
    app = wx.App()
    MyFrame()
    app.MainLoop()