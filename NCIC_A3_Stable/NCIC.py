# -*- coding: utf-8 -*- 
import wx
import wx.lib.agw.hyperlink as hl
from NCIC_IO import ncio
import NCIC_Lib as ncl

from threading import Thread
from pubsub import pub

OLD_FOLD = u".\\CompareFolder"
NEW_FOLD = u".\\CompareFolder"

STOP_THREAD=False

class NCBox ( wx.Dialog ):
	def __init__(self, tbody, *args, **kw):
		super(NCBox, self).__init__(*args, **kw)
		parentBX = wx.BoxSizer( wx.VERTICAL )

		self.hpl = hl.HyperLinkCtrl(self, -1, "NCIC", URL="https://nghichcode.com/")
		self.stxt = wx.StaticText( self, wx.ID_ANY, tbody )
		parentBX.Add( self.stxt, 0, wx.ALL, 5 )
		parentBX.Add( self.hpl, 0, wx.ALL, 5 )

		self.SetSizer( parentBX )
		self.Layout()
		parentBX.Fit( self )		
		self.Centre( wx.BOTH )

		self.Bind(wx.EVT_CLOSE, self.on_exit)

	def on_exit( self, event ):
		self.Destroy()

class NcImageCheck ( wx.Frame ):
	
	def __init__(self, *args, **kw):
		super(NcImageCheck, self).__init__(*args, **kw)
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		# MenuBar
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu2 = wx.Menu()
		self.mitGuide = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Guide", "\tNCIC User Guide", wx.ITEM_NORMAL )
		self.mitExit = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Exit", "\tExit NCIC", wx.ITEM_NORMAL )
		self.m_menu2.Append( self.mitGuide )
		self.m_menu2.AppendSeparator()
		self.m_menu2.Append( self.mitExit )
		self.m_menubar1.Append( self.m_menu2, u"File" ) 
		
		self.m_menu3 = wx.Menu()
		self.mitAbout = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"About", "\tInformation About NCIC", wx.ITEM_NORMAL )
		self.m_menu3.Append( self.mitAbout )
		self.m_menubar1.Append( self.m_menu3, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		# Body
		bSizerRoot = wx.BoxSizer( wx.VERTICAL )
		sbSizerChild = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"NC Image Check" ), wx.VERTICAL )
		# CS1
		bSizerCS1 = wx.BoxSizer( wx.VERTICAL )
		sbSizerChild.Add( bSizerCS1, 1, wx.EXPAND, 5 )
		# CS2
		gbSizerCS1 = wx.GridBagSizer( 0, 0 )
		gbSizerCS1.SetFlexibleDirection( wx.BOTH )
		gbSizerCS1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		self.m_staticText10 = wx.StaticText( sbSizerChild.GetStaticBox(), wx.ID_ANY, u"An Old Folder", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		self.m_dirPicker010 = wx.DirPickerCtrl( sbSizerChild.GetStaticBox(), wx.ID_ANY, OLD_FOLD, u"Select a folder", wx.DefaultPosition, wx.Size( 350,-1 ), wx.DIRP_DEFAULT_STYLE )
		
		gbSizerCS1.Add( self.m_staticText10, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 8 )
		gbSizerCS1.Add( self.m_dirPicker010, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 4 )

		sbSizerChild.Add( gbSizerCS1, 1, wx.EXPAND, 5 )
		# CS3
		gbSizerCS2 = wx.GridBagSizer( 0, 0 )
		gbSizerCS2.SetFlexibleDirection( wx.BOTH )
		gbSizerCS2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		self.m_staticText11 = wx.StaticText( sbSizerChild.GetStaticBox(), wx.ID_ANY, u"A  New Folder", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_dirPicker011 = wx.DirPickerCtrl( sbSizerChild.GetStaticBox(), wx.ID_ANY, NEW_FOLD, u"Select a folder", wx.DefaultPosition, wx.Size( 350,-1 ), wx.DIRP_DEFAULT_STYLE )
		
		gbSizerCS2.Add( self.m_staticText11, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 8 )
		gbSizerCS2.Add( self.m_dirPicker011, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 4 )

		sbSizerChild.Add( gbSizerCS2, 1, wx.EXPAND, 5 )

		# CS4
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		bSizerCS10 = wx.BoxSizer( wx.HORIZONTAL )
		self.m_staticText2 = wx.StaticText( sbSizerChild.GetStaticBox(), wx.ID_ANY, u"      Top IP(x)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_textCtrl1 = wx.TextCtrl( sbSizerChild.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		
		bSizerCS10.Add( self.m_staticText2, 0, wx.ALL, 8 )
		bSizerCS10.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		gSizer1.Add( bSizerCS10, 1, wx.EXPAND, 5 )
		
		bSizerCS11 = wx.BoxSizer( wx.HORIZONTAL )
		self.m_staticText3 = wx.StaticText( sbSizerChild.GetStaticBox(), wx.ID_ANY, u"      Top IP(y)", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_textCtrl2 = wx.TextCtrl( sbSizerChild.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		
		bSizerCS11.Add( self.m_staticText3, 0, wx.ALL, 8 )
		bSizerCS11.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		gSizer1.Add( bSizerCS11, 1, wx.EXPAND, 5 )

		sbSizerChild.Add( gSizer1, 1, wx.EXPAND, 5 )
		# CS5
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizerCS20 = wx.BoxSizer( wx.HORIZONTAL )
		self.m_staticText4 = wx.StaticText( sbSizerChild.GetStaticBox(), wx.ID_ANY, u"Bottom IP(x)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		self.m_textCtrl3 = wx.TextCtrl( sbSizerChild.GetStaticBox(), wx.ID_ANY, u"-1", wx.DefaultPosition, wx.DefaultSize, 0 )
		
		bSizerCS20.Add( self.m_staticText4, 0, wx.ALL, 8 )
		bSizerCS20.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
		gSizer2.Add( bSizerCS20, 1, wx.EXPAND, 5 )

		bSizerCS21 = wx.BoxSizer( wx.HORIZONTAL )
		self.m_staticText5 = wx.StaticText( sbSizerChild.GetStaticBox(), wx.ID_ANY, u"Bottom IP(y)", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_textCtrl4 = wx.TextCtrl( sbSizerChild.GetStaticBox(), wx.ID_ANY, u"40", wx.DefaultPosition, wx.DefaultSize, 0 )
		
		bSizerCS21.Add( self.m_staticText5, 0, wx.ALL, 8 )
		bSizerCS21.Add( self.m_textCtrl4, 0, wx.ALL, 5 )
		gSizer2.Add( bSizerCS21, 1, wx.EXPAND, 5 )

		sbSizerChild.Add( gSizer2, 1, wx.EXPAND, 5 )
		# CS6
		gSizer3 = wx.GridSizer( 0, 1, 0, 0 )
		
		bSizerCS30 = wx.BoxSizer( wx.HORIZONTAL )
		self.m_staticText6 = wx.StaticText( sbSizerChild.GetStaticBox(), wx.ID_ANY, u"Accurate (%)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		self.m_textCtrl5 = wx.TextCtrl( sbSizerChild.GetStaticBox(), wx.ID_ANY, u"1.5", wx.DefaultPosition, wx.DefaultSize, 0 )

		bSizerCS30.Add( self.m_staticText6, 0, wx.ALL, 8 )
		bSizerCS30.Add( self.m_textCtrl5, 0, wx.ALL, 5 )
		gSizer3.Add( bSizerCS30, 1, wx.EXPAND, 5 )

		sbSizerChild.Add( gSizer3, 1, wx.EXPAND, 5 )
		# CS8
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button2 = wx.Button( sbSizerChild.GetStaticBox(), wx.ID_ANY, u"Execute!!!", wx.DefaultPosition, wx.Size( 320,80 ), 0 )
		self.m_button2.SetFont( wx.Font( 16, 70, 90, 92, False, wx.EmptyString ) )
		self.m_button2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		bSizer4.Add( self.m_button2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sbSizerChild.Add( bSizer4, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		bSizerRoot.Add( sbSizerChild, 1, wx.EXPAND, 5 )

		self.SetSizer( bSizerRoot )
		self.Layout()
		self.m_statusBar = self.CreateStatusBar()
		self.SetStatusText("\tWelcome to NC Image Check!")

		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_dirPicker010.Bind( wx.EVT_DIRPICKER_CHANGED, self.set_old_folder )
		self.m_dirPicker011.Bind( wx.EVT_DIRPICKER_CHANGED, self.set_new_folder )
		self.m_button2.Bind( wx.EVT_BUTTON, self.start_compare )
		# Menu
		self.Bind( wx.EVT_MENU, self.on_guide, id = self.mitGuide.GetId() )
		self.Bind( wx.EVT_MENU, self.on_exit, id = self.mitExit.GetId() )
		self.Bind(wx.EVT_CLOSE, self.on_exit)
		self.Bind( wx.EVT_MENU, self.on_about, id = self.mitAbout.GetId() )
		pub.subscribe(self.updateDisplay, "update")
	
	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def updateDisplay(self,msg):
		self.m_button2.SetLabel(msg)
		if ( msg.find("Stat")<0 ) :
			self.m_button2.Enable()

	def set_old_folder( self, event ):
		global OLD_FOLD
		OLD_FOLD = event.GetPath()
		print(OLD_FOLD)
	def set_new_folder( self, event ):
		global NEW_FOLD
		NEW_FOLD = event.GetPath()
		print(NEW_FOLD)
	
	def ncth(self,cpfdo,cpfdn, *kws):
		pcrt,ipsx,ipsy,ipex,ipey = kws
		for rs in ncl.get_data(cpfdo,cpfdn, pcrt,ipsx,ipsy,ipex,ipey):
			global STOP_THREAD
			if (STOP_THREAD): break;
			wx.CallAfter(pub.sendMessage, "update", msg=rs)
		# wx.CallAfter(pub.sendMessage, "update", msg="success")

	def start_compare( self, event ):
		try:
			ipsx = int(self.m_textCtrl1.GetLineText(0))
			ipsy = int(self.m_textCtrl2.GetLineText(0))
			ipex = int(self.m_textCtrl3.GetLineText(0))
			ipey = int(self.m_textCtrl4.GetLineText(0))
			pcrt = float(self.m_textCtrl5.GetLineText(0))
		except ValueError as e:
			self.m_button2.SetLabel("Value Error")
			print("ValueError",e)
			return
		global OLD_FOLD
		global NEW_FOLD
		btn = event.GetEventObject()
		btn.Disable()
		NC_TH=Thread(target=self.ncth, args=(OLD_FOLD, NEW_FOLD, pcrt,ipsx,ipsy,ipex,ipey))
		NC_TH.start()

	def on_guide( self, event ):
		nb=NCBox(
			r"""
0. Your folders must have same length of image :
* Example
	|-\Old_Image_Folder\image00A.png
	|-\Old_Image_Folder\image01A.png
	...
	|-\Old_Image_Folder\FolderToCpx1
	|-\Old_Image_Folder\FolderToCpx1\image1A.png
	|-\Old_Image_Folder\FolderToCpx1\image2A.png
	...
	|-\Old_Image_Folder\FolderToCpx2
	|-\Old_Image_Folder\FolderToCpx2\image3A.png
	|-\Old_Image_Folder\FolderToCpx2\image4A.png
	...
	|-\New_Image_Folder\image00B.png
	|-\New_Image_Folder\image01B.png
	...
	|-\New_Image_Folder\FolderToCpx1
	|-\New_Image_Folder\FolderToCpx1\image1B.png
	|-\New_Image_Folder\FolderToCpx1\image2B.png
	...
	|-\New_Image_Folder\FolderToCpx2
	|-\New_Image_Folder\FolderToCpx2\image3B.png
	|-\New_Image_Folder\FolderToCpx2\image4B.png
	...
	...

1. Step 1: Click Browse to choose your folder.

* Default is : ".\CompareFolder"

2. Step 2: Set ignore point (pixel)
* IP is ignore point. You must set Top(x,y) and Bottom(x,y) ignore point!	
* Require : Top<Bottom .
* Enter -1 => ignore all
	Example : Top(0,0) , Bottom(-1,40) : Ignore all from (0,0) to ([image_width],40)

3. Step 3: Set Accurate (%).
	Example : 1.5%
4. Step 4: Click Execute.
	Result in ".\[parent_of_old_folder]\RESULT_OUT"
	AND .\[parent_of_old_folder]\RESULT_OUT_A2.csv
			""",
			None,
			title="NCIC User Guide",
			style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
		)
		nb.Show()

	def on_exit( self, event ):
		global STOP_THREAD
		STOP_THREAD = True
		self.Destroy()
		wx.GetApp().ExitMainLoop()
	
	def on_about( self, event ):
		nb=NCBox(
			"""
Name :  NCIC
Version : 2.2
Last release : 12/07/2019
Contact : nghichcode@gmail.com
COPYRIGHT @2019 nghichcode
			""",
			None,
			title="NCIC About",
			style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
		)
		nb.Show()

# Start App
if (ncio):
	app = wx.App()
	nic = NcImageCheck(
		None,
		title='NC Image Check',
		size = wx.Size( 500,400 ), style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
		)
	nic.Show()
	app.MainLoop()