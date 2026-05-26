"""
This is going ot be used for the UI and other front end items.
This is going to be linked to the DB


Look into: https://realpython.com/python-gui-with-wxpython/
Another look into: https://wiki.wxpython.org/How%20to%20Learn%20wxPython

MacOS has some more setup from what I've read, I am going to look into this a little bit later.
Running this on "MacOS Tahoe", M1 Max Macbook Pro

"""
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

class Tab(wx.Panel):
    def __init__(self, parent,label):
        wx.Panel.__init__(self, parent, -1)
        super().__init__(parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        text = wx.StaticText(self, 0, label=label)
        sizer.Add(text, 0, wx.ALL| wx.CENTER, 10)
        self.SetSizer(sizer)

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title="WxTest", size=(400,300))

        #Make our notebook (tab control), this is teh tab container
        notebook = wx.Notebook(self)

    # Each tab is a wx.panel
    # Can bind events like "EVT_NOTEBOOK_PAGE_CHANGED" to detect tab changes.
        # Create a tab page(s)
        tab1 = Tab(notebook, "Tab 1")
        tab2 = Tab(notebook, "Tab 2")

        button = wx.Button(tab1, -1, "Button 1")


        Button2 = wx.Button(tab2, -1, "Button 2",pos=(100,100))

        #Add our Notebook things
        notebook.AddPage(tab1, "Tab 1")
        notebook.AddPage(tab2, "Tab 2")


        #Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.EXPAND)
        self.SetSizer(sizer)

        self.Centre()
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    MyFrame()
    app.MainLoop()