import wx
import wx.xrc
import threading
import time
import random
import pytz
import urllib.request
import datetime
import time
import json
from xlrd import open_workbook

global s_time1, s_time2,x_pos,y_pos
x_pos="89"
y_pos="90"
s_time1=""
s_time2=""

class Position:
    x_pos="89"
    y_pos="91"
    def setpos(self,x_pos,y_pos):
        self.x_pos=x_pos
        self.y_pos=y_pos
    def getx_pos(self):
        return self.x_pos
    def gety_pos(self):
        return self.y_pos


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
        self.weatherPanel = WeatherPanel(self)
        self.dock = Dock(self)

        self.weatherPanel.Bind(wx.EVT_LEFT_DOWN, self.OnLeftdown_weather)
        self.weatherPanel.weather_bitmap.Bind(wx.EVT_LEFT_DOWN, self.OnLeftdown_weather)
        self.weatherPanel.w_text1.Bind(wx.EVT_LEFT_DOWN, self.OnLeftdown_weather)
        self.weatherPanel.w_text2.Bind(wx.EVT_LEFT_DOWN, self.OnLeftdown_weather)
        self.weatherPanel.w_text3.Bind(wx.EVT_LEFT_DOWN, self.OnLeftdown_weather)


    def OnLeftdown_weather(self,event):
        if WeatherDetailPanel.isOpen == False:
            print("A")
            self.w_detailPanel = WeatherDetailPanel(self)
            WeatherDetailPanel.isOpen = True



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
        wx.Panel.__init__(self, parent, pos=wx.Point(50, 50), size=wx.Size(200, 200))
        self.SetBackgroundColour(wx.Colour(10, 10, 10))


        self.t_text1 = wx.StaticText(self, label=str(s_time1), pos=(15, 40), size=(80, 50))
        self.t_text1.SetFont(wx.Font(30, 75, 90, 90, False, "210 Appgulim"))
        self.t_text1.SetForegroundColour(wx.Colour(255, 255, 255))

        self.t_text2 = wx.StaticText(self, label=str(s_time1), pos=(1, 90), size=(80, 50))
        self.t_text2.SetFont(wx.Font(15, 75, 90, 90, False, "210 Appgulim"))
        self.t_text2.SetForegroundColour(wx.Colour(255, 255, 255))
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftdown)
        self.t_text1.Bind(wx.EVT_LEFT_DOWN, self.OnLeftdown)
        self.t_text2.Bind(wx.EVT_LEFT_DOWN, self.OnLeftdown)


        t1 = ThreadClass1(self.t_text1)
        t1.daemon = True
        t1.start()
        t2 = ThreadClass2(self.t_text2)
        t2.dameon = True
        t2.start()


    def OnLeftdown(self,event):
        wx.MessageBox("달력출력","",wx.OK)


class ThreadClass1(threading.Thread):
    def __init__(self, text):
        threading.Thread.__init__(self)
        self.text = text
    def run(self):
        #print("A")
        while True:
            #print("A")
            dt=datetime.datetime.now()
            c_time = time.strftime("%X",time.localtime(time.time()))
            s_time1 = c_time


           # print(s_time1)
            #self.text.SetLabel(str(s_time))
            self.text.SetLabel(s_time1)

            time.sleep(1)
class ThreadClass2(threading.Thread):
    def __init__(self, text):
        threading.Thread.__init__(self)
        self.text = text
    def run(self):
       # print("A")
        while True:
            #print("A")
            dt=datetime.datetime.now()
            wday = time.strftime("%a",time.localtime(time.time()))
            mon =  time.strftime("%B",time.localtime(time.time()))
            s_time2 = wday+", "+mon+" "+str(dt.now().day)+" "+str(dt.now().year)

            #print(s_time2)
            #self.text.SetLabel(str(s_time))
            self.text.SetLabel(s_time2)

            time.sleep(1)

class WeatherPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, pos=wx.Point(300, 50), size=wx.Size(250, 250), style=wx.STATIC_BORDER)
        self.SetBackgroundColour(wx.Colour(15, 15, 15))

        self.weather_bitmap = wx.StaticBitmap(self, bitmap= show_result_bitmap(), pos=(10,30),size=(100,100))

        self.w_text1 = wx.StaticText(self, label=show_result1(),pos=(115,45),size=(50,50))
        self.w_text1.SetForegroundColour(wx.Colour(255, 255, 255))
        self.w_text1.SetFont(wx.Font(30, 75, 90, 90, False, "210 Appgulim"))

        self.w_text2 = wx.StaticText(self, label=show_result2(), pos=(115, 100), size=(50, 50))
        self.w_text2.SetForegroundColour(wx.Colour(255, 255, 255))
        self.w_text2.SetFont(wx.Font(13, 75, 90, 90, False, "210 Appgulim"))

        self.w_text3 = wx.StaticText(self, label=show_result3(), pos=(10, 140), size=(200, 20))
        self.w_text3.SetForegroundColour(wx.Colour(255, 255, 255))
        self.w_text3.SetFont(wx.Font(9, 75, 90, 90, False, "210 Appgulim"))

        pos_text="위치 : ("+x_pos+","+y_pos+")"
        self.w_text4 = wx.StaticText(self, label=pos_text, pos=(10, 170), size=(100, 20))
        self.w_text4.SetForegroundColour(wx.Colour(255, 255, 255))
        self.w_text4.SetFont(wx.Font(9, 75, 90, 90, False, "210 Appgulim"))

        m_comboBoxChoices1 = self.GetList()
        self.m_comboBox = wx.ComboBox(self, wx.ID_ANY, u"지역선택(시/도)", pos=(130, 170), size=wx.Size(100, -1),choices=m_comboBoxChoices1)
        self.m_comboBox.SetOwnBackgroundColour(wx.Colour(0, 0, 0))
        self.m_comboBox.SetOwnForegroundColour(wx.Colour(255, 255, 255))
        # self.m_comboBox.GetStringSelection()
        self.selection_text1 = "0"
        self.selection_text2 = "0"
        self.selection_text3 = "0"
        self.m_comboBox.Bind(wx.EVT_COMBOBOX, self.OnComboClick1)
        '''
        m_comboBoxChoices2 = self.GetList(3)
        self.m_comboBox = wx.ComboBox(self, wx.ID_ANY, u"지역선택(구/군)", pos=(130, 195), size=wx.Size(100, -1),
                                      choices=m_comboBoxChoices2)
        self.m_comboBox.SetOwnBackgroundColour(wx.Colour(0, 0, 0))
        self.m_comboBox.SetOwnForegroundColour(wx.Colour(255, 255, 255))
        # self.m_comboBox.GetStringSelection()
        self.selection_text = ""
        self.m_comboBox.Bind(wx.EVT_COMBOBOX, self.OnComboClick)

        m_comboBoxChoices3 = self.GetList(4)
        self.m_comboBox = wx.ComboBox(self, wx.ID_ANY, u"지역선택(동)", pos=(130, 220), size=wx.Size(100, -1),
                                      choices=m_comboBoxChoices3)
        self.m_comboBox.SetOwnBackgroundColour(wx.Colour(0, 0, 0))
        self.m_comboBox.SetOwnForegroundColour(wx.Colour(255, 255, 255))
        # self.m_comboBox.GetStringSelection()
        self.selection_text = ""
        self.m_comboBox.Bind(wx.EVT_COMBOBOX, self.OnComboClick)
        '''
    def GetList(self):
        wb = open_workbook('C:\\Users\\lg\\Desktop\\스마트미러_격자_위경도.xlsx')
        ws = wb.sheet_by_index(0)
        list1 = []
        for sheet in wb.sheets():
            # print (sheet.name)
            col1 = sheet.col(2)
            for r in col1:
                if r.value == ("1단계"):
                    pass
                else:
                    list1.append(r.value)

        list1 = list(set(list1))
        list1.sort()
        return list1
    def GetList2(self):
        wb = open_workbook('C:\\Users\\lg\\Desktop\\스마트미러_격자_위경도.xlsx')
        ws = wb.sheet_by_index(0)
        list1 = []
        num_rows = ws.nrows
        for i in range(num_rows):
            if ws.cell_value(i, 3)==("2단계"):
                pass
            elif ws.cell_value(i,2)!=self.selection_text1:
                pass
            else:
                list1.append(ws.cell_value(i,3))

        list1 = list(set(list1))
        list1.sort()
        return list1
    def GetList3(self):
        wb = open_workbook('C:\\Users\\lg\\Desktop\\스마트미러_격자_위경도.xlsx')
        ws = wb.sheet_by_index(0)
        list1 = []
        num_rows = ws.nrows
        for i in range(num_rows):
            if ws.cell_value(i, 4)==("3단계"):
                pass
            elif ws.cell_value(i,2)!=self.selection_text1:
                pass
            elif ws.cell_value(i,3)!=self.selection_text2:
                pass
            else:
                list1.append(ws.cell_value(i,4))

        list1 = list(set(list1))
        list1.sort()
        return list1
    def OnComboClick1(self, event):
        self.selection_text1 = self.m_comboBox.GetStringSelection()
        self.w_text4.Destroy()
        self.w_text5 = wx.StaticText(self, label=self.selection_text1, pos=(10, 170), size=(100, 20))
        self.w_text5.SetForegroundColour(wx.Colour(255, 255, 255))
        self.w_text5.SetFont(wx.Font(9, 75, 90, 90, False, "210 Appgulim"))

        m_comboBoxChoices2 = self.GetList2()
        self.m_comboBox2 = wx.ComboBox(self, wx.ID_ANY, u"지역선택(구/군)", pos=(130, 195), size=wx.Size(100, -1),choices=m_comboBoxChoices2)
        self.m_comboBox2.SetOwnBackgroundColour(wx.Colour(0, 0, 0))
        self.m_comboBox2.SetOwnForegroundColour(wx.Colour(255, 255, 255))
        # self.m_comboBox.GetStringSelection()
        self.m_comboBox2.Bind(wx.EVT_COMBOBOX, self.OnComboClick2)
        pass

    def OnComboClick2(self, event):
        self.selection_text2 = self.m_comboBox2.GetStringSelection()
        self.w_text6 = wx.StaticText(self, label=self.selection_text2, pos=(10, 195), size=(100, 20))
        self.w_text6.SetForegroundColour(wx.Colour(255, 255, 255))
        self.w_text6.SetFont(wx.Font(9, 75, 90, 90, False, "210 Appgulim"))
        m_comboBoxChoices3 = self.GetList3()
        self.m_comboBox3 = wx.ComboBox(self, wx.ID_ANY, u"지역선택(동)", pos=(130, 220), size=wx.Size(100, -1),
                                      choices=m_comboBoxChoices3)
        self.m_comboBox3.SetOwnBackgroundColour(wx.Colour(0, 0, 0))
        self.m_comboBox3.SetOwnForegroundColour(wx.Colour(255, 255, 255))
        # self.m_comboBox.GetStringSelection()
        #self.selection_text = ""
        self.m_comboBox3.Bind(wx.EVT_COMBOBOX, self.OnComboClick3)
        pass

    def OnComboClick3(self, event):
        self.selection_text3 = self.m_comboBox3.GetStringSelection()
        self.w_text7 = wx.StaticText(self, label=self.selection_text3, pos=(10, 220), size=(100, 20))
        self.w_text7.SetForegroundColour(wx.Colour(255, 255, 255))
        self.w_text7.SetFont(wx.Font(9, 75, 90, 90, False, "210 Appgulim"))

        self.m_comboBox.Destroy()
        self.m_comboBox2.Destroy()

        self.btn=wx.Button(self,label="변경",pos=(130,170), size=wx.Size(50,-1))
        self.btn.SetOwnBackgroundColour(wx.Colour(0, 0, 0))
        self.btn.SetOwnForegroundColour(wx.Colour(255, 255, 255))
        self.btn.Bind(wx.EVT_BUTTON,self.OnBtnClick)
        pass
        #print("누가parent:")
        #print(parent)
    def OnBtnClick(self,event):
        global x_pos,y_pos
        wb = open_workbook('C:\\Users\\lg\\Desktop\\스마트미러_격자_위경도.xlsx')
        ws = wb.sheet_by_index(0)
        num_rows = ws.nrows
        category1 = self.selection_text1
        category2 = self.selection_text2
        category3 = self.selection_text3
        for i in range(num_rows):
            if ws.cell_value(i, 2) == category1 and ws.cell_value(i, 3) == category2 and ws.cell_value(i,4) == category3:
                x_pos=ws.cell_value(i, 5)
                y_pos=ws.cell_value(i, 6)
                print(category1 + category2 + category3 + ":" + ws.cell_value(i, 5) + "," + ws.cell_value(i, 6))
        self.btn.Destroy()
        self.weather_bitmap.Destroy()
        self.w_text1.Destroy()
        self.w_text2.Destroy()
        self.w_text3.Destroy()
        #self.w_text4.Destroy()
        self.w_text5.Destroy()
        self.w_text6.Destroy()
        self.w_text7.Destroy()
        self.m_comboBox3.Destroy()

        self.weather_bitmap = wx.StaticBitmap(self, bitmap=show_result_bitmap(), pos=(10, 30), size=(100, 100))

        self.w_text1 = wx.StaticText(self, label=show_result1(), pos=(115, 45), size=(50, 50))
        self.w_text1.SetForegroundColour(wx.Colour(255, 255, 255))
        self.w_text1.SetFont(wx.Font(30, 75, 90, 90, False, "210 Appgulim"))

        self.w_text2 = wx.StaticText(self, label=show_result2(), pos=(115, 100), size=(50, 50))
        self.w_text2.SetForegroundColour(wx.Colour(255, 255, 255))
        self.w_text2.SetFont(wx.Font(13, 75, 90, 90, False, "210 Appgulim"))

        self.w_text3 = wx.StaticText(self, label=show_result3(), pos=(10, 140), size=(200, 20))
        self.w_text3.SetForegroundColour(wx.Colour(255, 255, 255))
        self.w_text3.SetFont(wx.Font(9, 75, 90, 90, False, "210 Appgulim"))

        pos_text = "(" + x_pos + "," + y_pos+ ")\n"+category1+" \n>"+category2+" \n>"+category3
        self.w_text4 = wx.StaticText(self, label=pos_text, pos=(10, 170), size=(100, 30))
        self.w_text4.SetForegroundColour(wx.Colour(255, 255, 255))
        self.w_text4.SetFont(wx.Font(9, 75, 90, 90, False, "210 Appgulim"))

        m_comboBoxChoices1 = self.GetList()
        self.m_comboBox = wx.ComboBox(self, wx.ID_ANY, u"지역선택(시/도)", pos=(130, 170), size=wx.Size(100, -1),
                                      choices=m_comboBoxChoices1)
        self.m_comboBox.SetOwnBackgroundColour(wx.Colour(0, 0, 0))
        self.m_comboBox.SetOwnForegroundColour(wx.Colour(255, 255, 255))
        self.m_comboBox.Bind(wx.EVT_COMBOBOX, self.OnComboClick1)
        pass
def get_weather_data():
    api_date, api_time = get_api_date()
    url = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?"
    key = "serviceKey=" + "Dc6ewA1eR8iB5JzsB5vrC8Bt9Xs%2F43rSAnXksoR3ZYoaAs3qb%2F8sfb8zeMdDtg4ZHrnEO4j1aSQCQshB5h2P1A%3D%3D"
    date = "&base_date=" + api_date
    time = "&base_time=" + api_time
    #x_pos=input("x좌표입력 : ")
    #y_pos=input("y좌표입력 : ")
    #x_pos="89"
    #y_pos="91"
    print("("+ x_pos +","+ y_pos+")")
    nx = "&nx="+x_pos
    ny = "&ny="+y_pos
    numOfRows = "&numOfRows=100"
    type = "&_type=json"
    api_url = url + key + date + time + nx + ny + numOfRows + type

    #print(api_url)
    data = urllib.request.urlopen(api_url).read().decode('utf8')
    #print(data)
    data_json = json.loads(data)
    #print(data_json)
    parsed_json = data_json['response']['body']['items']['item']
    #print(parsed_json[0])

    target_date = parsed_json[0]['fcstDate']  # get date and time
    target_time = parsed_json[0]['fcstTime']
    #print(type(target_time))
    #print(target_date)
    #print( parsed_json)
    #print(parsed_json[0])

    date_calibrate = target_date  # date of TMX, TMN
    if target_time > 1300:
        date_calibrate = str(int(target_date)+1)

    passing_data = {}
    check=0
    for one_parsed in parsed_json:
        if one_parsed['fcstDate'] == target_date and one_parsed['fcstTime'] == target_time:  # get today's data
            passing_data[one_parsed['category']] = one_parsed['fcstValue']

        if one_parsed['category'] == 'TMX' or one_parsed['category'] == 'TMN':  # TMX, TMN at calibrated day
            passing_data[one_parsed['category']] = one_parsed['fcstValue']

        if one_parsed['category'] =="PTY" and one_parsed['fcstValue']>0:
            check = 1
    if check==1:
        passing_data['umbrella']=1
    else :
        passing_data['umbrella']=0


    return passing_data
class WeatherDetailPanel(wx.Panel):
    isOpen = False
    def __init__(self,parent):
        wx.Panel.__init__(self,parent,pos=wx.Point(50,300),size=wx.Size(500,150), style=wx.STATIC_BORDER)
        self.SetBackgroundColour(wx.Colour(15,15,15))
        #show_detail_result()


        #self.text = wx.StaticText(self, label="날씨상세정보출력", pos=(90, 70), size=(50, 50))
        #self.text.SetFont(
        #    wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "210 Appgulim"))
        #self.text.SetForegroundColour(wx.Colour(255, 255, 255))
        get_data = get_weather_data_detail()

        m_comboBoxChoices = list(get_data.keys())
        self.m_comboBox = wx.ComboBox(self, wx.ID_ANY, u"시간선택", pos=(250,10), size=wx.Size(200,-1), choices=m_comboBoxChoices)
        self.m_comboBox.SetOwnBackgroundColour(wx.Colour(0,0,0))
        self.m_comboBox.SetOwnForegroundColour(wx.Colour(255, 255, 255))
        #self.m_comboBox.GetStringSelection()
        self.selection_text=""
        self.m_comboBox.Bind(wx.EVT_COMBOBOX,self.OnComboClick)
        self.weather_bitmap = wx.StaticBitmap(self, bitmap=show_result_bitmap(), pos=(10, 30), size=(100, 100))

        self.w_text1 = wx.StaticText(self, label=show_detail_result1(self.selection_text), pos=(115, 45), size=(50, 50))
        self.w_text1.SetForegroundColour(wx.Colour(255, 255, 255))
        self.w_text1.SetFont(wx.Font(30, 75, 90, 90, False, "210 Appgulim"))

        self.w_text2 = wx.StaticText(self, label=show_detail_result2(self.selection_text), pos=(250, 100), size=(50, 50))
        self.w_text2.SetForegroundColour(wx.Colour(255, 255, 255))
        self.w_text2.SetFont(wx.Font(13, 75, 90, 90, False, "210 Appgulim"))

        self.w_text3 = wx.StaticText(self, label=show_detail_result3(self.selection_text), pos=(115, 100),size=(50, 50))
        self.w_text3.SetForegroundColour(wx.Colour(255, 255, 255))
        self.w_text3.SetFont(wx.Font(13, 75, 90, 90, False, "210 Appgulim"))
        #show_detail_result(self.selection_text)


        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftdown)

    def OnComboClick(self,event):
        self.selection_text=self.m_comboBox.GetStringSelection()
        print(self.selection_text)
        self.weather_bitmap.Destroy()
        self.w_text1.Destroy()
        self.w_text2.Destroy()
        self.weather_bitmap = wx.StaticBitmap(self, bitmap=show_result_detail_bitmap(self.selection_text), pos=(10, 30), size=(100, 100))

        self.w_text1 = wx.StaticText(self, label=show_detail_result1(self.selection_text), pos=(115, 45), size=(50, 50))
        self.w_text1.SetForegroundColour(wx.Colour(255, 255, 255))
        self.w_text1.SetFont(wx.Font(30, 75, 90, 90, False, "210 Appgulim"))

        self.w_text2 = wx.StaticText(self, label=show_detail_result2(self.selection_text), pos=(250, 100), size=(50, 50))
        self.w_text2.SetForegroundColour(wx.Colour(255, 255, 255))
        self.w_text2.SetFont(wx.Font(13, 75, 90, 90, False, "210 Appgulim"))

        self.w_text3 = wx.StaticText(self, label=show_detail_result3(self.selection_text), pos=(115, 100),size=(50, 50))
        self.w_text3.SetForegroundColour(wx.Colour(255, 255, 255))
        self.w_text3.SetFont(wx.Font(13, 75, 90, 90, False, "210 Appgulim"))

    def OnLeftdown(self,event):
        #print(self.isOpen)
        WeatherDetailPanel.isOpen = False
        self.Destroy()
        #print(show_detail_result1(self.selection_text))
        #print(self.IsOpen())



def get_weather_data_detail():
    api_date, api_time = get_api_date()
    url = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?"
    key = "serviceKey=" + "Dc6ewA1eR8iB5JzsB5vrC8Bt9Xs%2F43rSAnXksoR3ZYoaAs3qb%2F8sfb8zeMdDtg4ZHrnEO4j1aSQCQshB5h2P1A%3D%3D"
    date = "&base_date=" + api_date
    time = "&base_time=" + api_time
    # x_pos=input("x좌표입력 : ")
    # y_pos=input("y좌표입력 : ")
    nx = "&nx=" + x_pos
    ny = "&ny=" + y_pos
    numOfRows = "&numOfRows=100"
    type = "&_type=json"
    api_url = url + key + date + time + nx + ny + numOfRows + type

    data = urllib.request.urlopen(api_url).read().decode('utf8')
    #print(data)
    data_json = json.loads(data)
    #print(data_json)
    parsed_json = data_json['response']['body']['items']['item']
    #print(parsed_json)
    #print(parsed_json[0])

    target_date = parsed_json[0]['fcstDate']  # get date and time
    target_time = parsed_json[0]['fcstTime']
    #print(type(parsed_json[0]['fcstTime']))

    passing_data = {}
    daycnt=0


    key=0
    for one_parsed in parsed_json:
        if one_parsed['category'] == 'POP':
            #passing_data[one_parsed['category']] = one_parsed['fcstValue']
            passing_data.update({key:(one_parsed['category'], one_parsed['fcstValue'], one_parsed['fcstDate'], one_parsed['fcstTime'])})
            key += 1


        if one_parsed['category'] == 'PTY':
            #passing_data[one_parsed['category']] = one_parsed['fcstValue']
            passing_data.update({key:(one_parsed['category'], one_parsed['fcstValue'], one_parsed['fcstDate'], one_parsed['fcstTime'])})
            key += 1

        if one_parsed['category'] == 'SKY':
            #passing_data[one_parsed['category']] = one_parsed['fcstValue']
            passing_data.update({key:(one_parsed['category'],one_parsed['fcstValue'],one_parsed['fcstDate'],one_parsed['fcstTime'])})
            key+=1

        if one_parsed['category'] == 'T3H':
            #passing_data[one_parsed['category']] = one_parsed['fcstValue']
            passing_data.update({key:(one_parsed['category'], one_parsed['fcstValue'], one_parsed['fcstDate'], one_parsed['fcstTime'])})
            key += 1
    final_passing_data={}
    #print(passing_data[0])
    for one_parsed in passing_data:
        time=str(passing_data[one_parsed][3])
        time=time[:2]+":"+time[2:]
        time=str(passing_data[one_parsed][2])+" "+time
        if time in final_passing_data:
            final_passing_data[time]=final_passing_data[time]+(passing_data[one_parsed][0], passing_data[one_parsed][1])
        else:
            final_passing_data[time]=(passing_data[one_parsed][0], passing_data[one_parsed][1])

    return final_passing_data

def get_api_date():
    standard_time = [2, 5, 8, 11, 14, 17, 20, 23]
    time_now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime('%H')
    time_plus_now=datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime('%H:%M:%S')
    #print("시간 : "+time_now)
    check_time = int(time_now) - 1
    day_calibrate = 0
    while not check_time in standard_time:
        check_time -= 1
        if check_time < 2:
            day_calibrate = 1
            check_time = 23

    date_now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime('%Y%m%d')
    #print("date : "+date_now)
    check_date = int(date_now) - day_calibrate

    return (str(check_date), (str(check_time) + '00'))
def show_result_bitmap():
    get_data = get_weather_data()

    if get_data["PTY"]==1:
        weather = wx.Bitmap("C:\\Users\\lg\\Desktop\\비.png")
    elif get_data["PTY"]==2:
        weather = wx.Bitmap("C:\\Users\\lg\\Desktop\\진눈깨비.png")
    elif get_data["PTY"]==3:
        weather = wx.Bitmap("C:\\Users\\lg\\Desktop\\눈.png")
    elif get_data["PTY"]==0 and get_data["SKY"]==1:
        weather=wx.Bitmap("C:\\Users\\lg\\Desktop\\맑음.png")
    elif get_data["PTY"]==0 and get_data["SKY"]==2:
        weather = wx.Bitmap("C:\\Users\\lg\\Desktop\\구름조금.png")
    elif get_data["PTY"]==0 and get_data["SKY"]==3:
        weather = wx.Bitmap("C:\\Users\\lg\\Desktop\\구름많음.png")
    elif get_data["PTY"]==0 and get_data["SKY"]==4:
        weather = wx.Bitmap("C:\\Users\\lg\\Desktop\\흐림.png")

    result=weather

    return result
def show_result_detail_bitmap(target_time):
    if target_time == "":
        return True
    get_data = get_weather_data_detail()

    if get_data[target_time][3]==1:
        weather = wx.Bitmap("C:\\Users\\lg\\Desktop\\비.png")
    elif get_data[target_time][3]==2:
        weather = wx.Bitmap("C:\\Users\\lg\\Desktop\\진눈깨비.png")
    elif get_data[target_time][3]==3:
        weather = wx.Bitmap("C:\\Users\\lg\\Desktop\\눈.png")
    elif get_data[target_time][3]==0 and get_data[target_time][5]==1:
        weather=wx.Bitmap("C:\\Users\\lg\\Desktop\\맑음.png")
    elif get_data[target_time][3]==0 and get_data[target_time][5]==2:
        weather = wx.Bitmap("C:\\Users\\lg\\Desktop\\구름조금.png")
    elif get_data[target_time][3]==0 and get_data[target_time][5]==3:
        weather = wx.Bitmap("C:\\Users\\lg\\Desktop\\구름많음.png")
    elif get_data[target_time][3]==0 and get_data[target_time][5]==4:
        weather = wx.Bitmap("C:\\Users\\lg\\Desktop\\흐림.png")

    result=weather

    return result
def show_result1():
    get_data = get_weather_data()
    current_tem = str(get_data['T3H'])+" ℃"
    result=current_tem

    return result
def show_result2():
    get_data = get_weather_data()
    #print(get_data)
    h_tem = str(get_data['TMX'])+" ℃"
    l_tem = str(get_data['TMN'])+" ℃"

    if get_data["umbrella"]==0:
        comment="오늘은 눈이나 비가 안올예정이네요~     "
    elif get_data["umbrella"]==1:
        comment="오늘은 우산꼭! (비나 눈이 올예정이에요)"
    result=l_tem+"/"+h_tem

    return result
def show_result3():
    get_data = get_weather_data()
    if get_data["umbrella"]==0:
        comment="오늘은 눈이나 비가 안올예정이네요~ "
    elif get_data["umbrella"]==1:
        comment="오늘은 우산꼭! (비나 눈이 올예정이에요)"
    result=comment
    return result

def show_detail_result1(target_time):
    if target_time =="":
        return "ComboBox에서↑"
    get_data = get_weather_data_detail()
    tem="현재온도 : "+str(get_data[target_time][7])+" ℃"
    result = tem
    return result

def show_detail_result2(target_time):
    if target_time =="":
        return "찾고싶은 시간을 입력하세요"
    get_data=get_weather_data_detail()
    r_percent="강수확률 : "+str(get_data[target_time][1])+" %"
    result = r_percent
    return result

def show_detail_result3(target_time):
    if target_time == "":
        return " "
    get_data = get_weather_data_detail()
    if get_data[target_time][3]==1:
        weather = "비        "
    elif get_data[target_time][3]==2:
        weather = "진눈깨비   "
    elif get_data[target_time][3]==3:
        weather = "눈        "
    elif get_data[target_time][3]==0 and get_data[target_time][5]==1:
        weather="맑음        "
    elif get_data[target_time][3]==0 and get_data[target_time][5]==2:
        weather = "구름조금   "
    elif get_data[target_time][3]==0 and get_data[target_time][5]==3:
        weather = "구름많음   "
    elif get_data[target_time][3]==0 and get_data[target_time][5]==4:
        weather = "흐림      "

    return weather

class Dock(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, pos=wx.Point(30, 840), size=wx.Size(540, 40), style=wx.STATIC_BORDER)
        self.SetBackgroundColour(wx.Colour(15, 15, 15))

        self.text = wx.StaticText(self, label="DOCK", pos=(250, 0), size=(50, 40))
        self.text.SetFont(
            wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "210 Appgulim"))
        self.text.SetForegroundColour(wx.Colour(255, 255, 255))


if __name__ == "__main__":
    app = wx.App()

    frame = MirrorFrame()
    frame.Show()

    app.MainLoop()


