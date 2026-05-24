"""
This is going ot be used for the UI and other front end items.
This is going to be linked to the DB


Look into: https://realpython.com/python-gui-with-wxpython/
Another look into: https://wiki.wxpython.org/How%20to%20Learn%20wxPython

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
# How this looks as a class
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="Hello world")
        self.panel = wx.Panel(self)

        self.atext_ctrl = wx.TextCtrl(self.panel,pos=(5,5))
        my_btn = wx.Button(self.panel,label="Press Me!", pos=(5,55))

        self.Show()

# Our entry point for this script
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()

