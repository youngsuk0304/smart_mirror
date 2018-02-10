import wx
import wx.xrc
import threading
import time
import random

class DockPanel (wx.Panel):
    def __init__(self, parent, id=wx.ID_ANY, pos=(100,100), size=(400,700),style=wx.DOUBLE_BORDER):
        wx.Panel.__init__(self, parent=parent, id = id, pos=pos, size=size, style=style)

class MirrorFrame(wx.Frame):

    def __init__(self, parent=None):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(600, 900), style=0 | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(wx.Colour(0, 0, 0))
        self.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.Centre(wx.BOTH)
        self.schedulePanel = SchedulePanel(self)
        self.timePanel = TimePanel(self)
        self.wetherPanel = WetherPanel(self)
        self.dock = Dock(self)
        #self.dock.memoim.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLButtonDown)
        self.dock.memoim.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLButtonDown)


    def OnMouseLButtonDown(self, event):
        create_panel = DockPanel(self)
        create_panel.SetFont(wx.Font(15, 71, 90, 90, False, wx.EmptyString))
        #bus_panel.SetFocusIgnoringChildren(self)
        create_panel.SetForegroundColour(wx.Colour(0, 0, 255))
        create_panel.SetBackgroundColour(wx.Colour(255, 0, 0))
       
        



class SchedulePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, pos=wx.Point(50, 650), size=wx.Size(200, 150), style=wx.DOUBLE_BORDER)
        self.SetBackgroundColour(wx.Colour(15, 15, 15))

        self.text = wx.StaticText(self, label="일정", pos=(0, 0), size=(200, 150))
        self.text.SetFont(
            wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "210 Appgulim"))
        self.text.SetForegroundColour(wx.Colour(255, 255, 255))


class TimePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, pos=wx.Point(50, 50), size=wx.Size(200, 100))
        self.SetBackgroundColour(wx.Colour(10, 10, 10))

        self.text = wx.StaticText(self, label="시간", pos=(60, 40), size=(80, 50))
        self.text.SetFont(
            wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "210 Appgulim"))
        self.text.SetForegroundColour(wx.Colour(255, 255, 255))


class WetherPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, pos=wx.Point(300, 50), size=wx.Size(250, 150), style=wx.STATIC_BORDER)
        self.SetBackgroundColour(wx.Colour(15, 15, 15))

        self.text = wx.StaticText(self, label="날씨", pos=(90, 70), size=(50, 50))
        self.text.SetFont(
            wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "210 Appgulim"))
        self.text.SetForegroundColour(wx.Colour(255, 255, 255))

class Dock(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, pos=wx.Point(30, 810), size=wx.Size(540, 80), style=wx.STATIC_BORDER)

        self.SetBackgroundColour(wx.Colour(15, 15, 15))

        self.text = wx.StaticText(self, label="DOCK", pos=(250, 0), size=(50, 40))
        self.text.SetFont(
            wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "210 Appgulim"))
        self.text.SetForegroundColour(wx.Colour(255, 255, 255))

        self.memoim=wx.StaticBitmap(self, -1, wx.Bitmap("C:\\Users\Public\Pictures\Sample Pictures\\memo.png", wx.BITMAP_TYPE_PNG),pos=(0,0),size=(80,80))
        fashion = wx.StaticBitmap(self, -1,wx.Bitmap("C:\\Users\Public\Pictures\Sample Pictures\\fashion.png", wx.BITMAP_TYPE_PNG),pos=(80,0), size=(100, 80))





if __name__ == "__main__":
    app = wx.App()
    frame = MirrorFrame()
    frame.Show()

    app.MainLoop()


