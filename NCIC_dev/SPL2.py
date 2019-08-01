import threading,wx

ID_RUN=101
ID_RUN2=102

class MyFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title)
        panel = wx.Panel(self, -1)
        mainSizer=wx.BoxSizer(wx.HORIZONTAL)
        mainSizer.Add(wx.Button(panel, ID_RUN, "Click me"))
        mainSizer.Add(wx.Button(panel, ID_RUN2, "Click me too"))
        panel.SetSizer(mainSizer)
        mainSizer.Fit(self)
        self.Bind( wx.EVT_BUTTON, self.onRun, id = ID_RUN )
        self.Bind( wx.EVT_BUTTON, self.onRun2, id = ID_RUN2 )
        # wx.EVT_BUTTON(self, ID_RUN, self.onRun)
        # wx.EVT_BUTTON(self, ID_RUN2, self.onRun2)

    def onRun(self,event):
        print("Clicky!")
        wx.CallAfter(self.AfterRun, "I don't appear until after OnRun exits")
        s=input("Enter something:")
        print(s)

    def onRun2(self,event):
        t=threading.Thread(target=self.__run)
        t.start()

    def __run(self):
        wx.CallAfter(self.AfterRun, "I appear immediately (event handler\n exited when OnRun2 finished)")
        s=input("Enter something in this thread:")
        print(s)

    def AfterRun(self,msg):
        dlg=wx.MessageDialog(self, msg, "Called after", wx.OK|wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, "CallAfter demo")
        frame.Show(True)
        frame.Centre()
        return True

app = MyApp(0)
app.MainLoop()

# import cv2

# image = cv2.imread('io.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# print(len(gray),len(gray[0]))
# cv2.imshow('Original image',image)
# cv2.imshow('Gray image', gray)
  
# cv2.waitKey(0)
# cv2.destroyAllWindows()