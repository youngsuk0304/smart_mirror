import wx
import wx.xrc
import threading
import time
import random

class createPanel_memo_write(wx.Panel):

    def __init__(self, parent):
        Title = "제목 : "
        Memo = "내용 : "
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(400, 360), style=0)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        bSizer4.SetMinSize(wx.Size(400, 360))
        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.Point(0, 0), wx.Size(400, 40), wx.TAB_TRAVERSAL)
        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl3 = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       0 | wx.NO_BORDER)
        self.m_textCtrl3.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))
        self.m_textCtrl3.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.m_textCtrl3.AppendText(Title)
        bSizer6.Add(self.m_textCtrl3, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel3.SetSizer(bSizer6)
        self.m_panel3.Layout()
        bSizer4.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.Point(0, 40), wx.Size(400, 320), wx.TAB_TRAVERSAL)
        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl4 = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       0 | wx.NO_BORDER)
        self.m_textCtrl4.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))
        self.m_textCtrl4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.m_textCtrl4.AppendText(Memo)
        bSizer7.Add(self.m_textCtrl4, 9, wx.ALL | wx.EXPAND, 5)

        self.save = wx.StaticBitmap(self.m_panel4, wx.Bitmap("C:\\Users\Public\Pictures\Sample Pictures\\save_button1.png",wx.BITMAP_TYPE_PNG), wx.Size(50, 50))
        bSizer7.Add(self.save, 1, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.m_panel4.SetSizer(bSizer7)
        self.m_panel4.Layout()
        bSizer4.Add(self.m_panel4, 8, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer4)
        self.Layout()
        #self.save = wx.StaticBitmap(self, -1, wx.Bitmap("C:\\Users\Public\Pictures\Sample Pictures\\save_button1.png", wx.BITMAP_TYPE_PNG), pos=(340, 300), size=(50, 50))




class createPanel_memoim(wx.Panel):
    isOpen = False
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=(100,210), size=(400,430),style=wx.SUNKEN_BORDER)
        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.memoim = wx.StaticBitmap(self, -1, wx.Bitmap("C:\\Users\Public\Pictures\Sample Pictures\\button4.png",wx.BITMAP_TYPE_PNG), pos=(330, 360), size=(50, 50))
        self.memoim.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLButtonDown_memoim)

    def OnMouseLButtonDown_memoim(self, event):
        self.create_panel_memo_write = createPanel_memo_write(self)
        self.create_panel_memo_write.SetFont(wx.Font(15, 71, 90, 90, False, wx.EmptyString))
        createPanel_memoim.isOpen = True


class createPanel_fashion(wx.Panel):
    isOpen = False
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=(100,210), size=(400,430),style=wx.SUNKEN_BORDER)
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.SetBackgroundColour(wx.Colour(0, 0, 255))
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(bSizer1)
        self.Layout()


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
        self.dock.memoim.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLButtonDown_memoim)
        self.dock.fashion.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLButtonDown_fashion)
        #self.dock.memoim.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLButtonDown)
        #self.dock.memoim.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLButtonDown)
        self.create_panel = None


    def OnMouseLButtonDown_memoim(self, event):
        if createPanel_memoim.isOpen == False:
            self.create_panel_memoim = createPanel_memoim(self)
            self.create_panel_memoim.SetFont(wx.Font(15, 71, 90, 90, False, wx.EmptyString))
            createPanel_memoim.isOpen = True
        else:
            self.create_panel_memoim.Destroy()
            createPanel_memoim.isOpen =False
    def OnMouseLButtonDown_fashion(self, event):
        if createPanel_fashion.isOpen == False:
            self.create_panel_fashion = createPanel_fashion(self)
            self.create_panel_fashion.SetFont(wx.Font(15, 71, 90, 90, False, wx.EmptyString))
            #bus_panel.SetFocusIgnoringChildren(self)
            createPanel_fashion.isOpen = True
        else:
            self.create_panel_fashion.Destroy()
            createPanel_fashion.isOpen =False

       
        



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
        self.fashion = wx.StaticBitmap(self, -1,wx.Bitmap("C:\\Users\Public\Pictures\Sample Pictures\\fashion.png", wx.BITMAP_TYPE_PNG),pos=(80,0), size=(100, 80))





if __name__ == "__main__":
    app = wx.App()
    frame = MirrorFrame()
    frame.Show()

    app.MainLoop()


