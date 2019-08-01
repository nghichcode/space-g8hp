import time
import wx
 
from threading import Thread
# from wx.lib.pubsub import Publisher
from pubsub import pub
 
########################################################################
class TestThread(Thread):

	def __init__(self):
		"""Init Worker Thread Class."""
		Thread.__init__(self)
		self.start()	# start the thread

	def run(self):
		"""Run Worker Thread."""
		# This is the code executing in the new thread.
		for i in range(6):
			print("C1")
			time.sleep(2)
			wx.CallAfter(self.postTime, i)
		time.sleep(1)
		wx.CallAfter(pub.sendMessage, "update", msg="Thread finished!")
 
	#----------------------------------------------------------------------
	def postTime(self, amt):
		"""
		Send time to GUI
		"""
		amtOfTime = (amt + 1) * 10
		pub.sendMessage("update", msg=amtOfTime)
 
########################################################################
class MyForm(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, "Tutorial")
 
		# Add a panel so it looks the correct on all platforms
		panel = wx.Panel(self, wx.ID_ANY)
		self.displayLbl = wx.StaticText(panel, label="Amount of time since thread started goes here")
		self.btn = btn = wx.Button(panel, label="Start Thread")
 
		btn.Bind(wx.EVT_BUTTON, self.onButton)
 
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.displayLbl, 0, wx.ALL|wx.CENTER, 5)
		sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)
		panel.SetSizer(sizer)
 
		# create a pubsub receiver
		pub.subscribe(self.updateDisplay, "update")
 
	#----------------------------------------------------------------------
	def onButton(self, event):
		"""
		Runs the thread
		"""
		TestThread()
		self.displayLbl.SetLabel("Thread started!")
		btn = event.GetEventObject()
		btn.Disable()
 
	#----------------------------------------------------------------------
	def updateDisplay(self, msg):
		if isinstance(msg, int):
			self.displayLbl.SetLabel("Time since thread started: %s seconds" % msg)
		else:
			self.displayLbl.SetLabel("%s" % msg)
			self.btn.Enable()

class NC:
	c=10
	def __init__(self):
		pub.subscribe(self.sc, "sc")

	def gc(self):
		return (self.c)
	def sc(self,d):
		self.c=d

if __name__ == "__main__":
	app = wx.App()
	frame = MyForm().Show()
	app.MainLoop()

	# nc = NC()
	# nc.c=100
	# print(nc.gc())
	# pub.sendMessage("sc", d=5)
	# print(nc.gc())
	# wx.CallAfter(pub.sendMessage, 'sc', d=8)
	# print(nc.gc())