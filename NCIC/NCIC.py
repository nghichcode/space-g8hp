# -*- coding: utf-8 -*- 
import os

import wx
import wx.xrc
import wx.adv
import wx.lib.agw.hyperlink as hl
from NCIC_ION import ncio

COMPARE_FOLD = u".\\CompareFolder"

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
		self.m_staticText10 = wx.StaticText( sbSizerChild.GetStaticBox(), wx.ID_ANY, u"Select Folder", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		self.m_dirPicker2 = wx.DirPickerCtrl( sbSizerChild.GetStaticBox(), wx.ID_ANY, COMPARE_FOLD, u"Select a folder", wx.DefaultPosition, wx.Size( 350,-1 ), wx.DIRP_DEFAULT_STYLE )
		
		gbSizerCS1.Add( self.m_staticText10, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 8 )
		gbSizerCS1.Add( self.m_dirPicker2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 4 )

		sbSizerChild.Add( gbSizerCS1, 1, wx.EXPAND, 5 )
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
		self.m_textCtrl3 = wx.TextCtrl( sbSizerChild.GetStaticBox(), wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		
		bSizerCS20.Add( self.m_staticText4, 0, wx.ALL, 8 )
		bSizerCS20.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
		gSizer2.Add( bSizerCS20, 1, wx.EXPAND, 5 )

		bSizerCS21 = wx.BoxSizer( wx.HORIZONTAL )
		self.m_staticText5 = wx.StaticText( sbSizerChild.GetStaticBox(), wx.ID_ANY, u"Bottom IP(y)", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_textCtrl4 = wx.TextCtrl( sbSizerChild.GetStaticBox(), wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		
		bSizerCS21.Add( self.m_staticText5, 0, wx.ALL, 8 )
		bSizerCS21.Add( self.m_textCtrl4, 0, wx.ALL, 5 )
		gSizer2.Add( bSizerCS21, 1, wx.EXPAND, 5 )

		sbSizerChild.Add( gSizer2, 1, wx.EXPAND, 5 )
		# CS6
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizerCS30 = wx.BoxSizer( wx.HORIZONTAL )
		self.m_staticText6 = wx.StaticText( sbSizerChild.GetStaticBox(), wx.ID_ANY, u"Accurate (w)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		self.m_textCtrl5 = wx.TextCtrl( sbSizerChild.GetStaticBox(), wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )

		bSizerCS30.Add( self.m_staticText6, 0, wx.ALL, 8 )
		bSizerCS30.Add( self.m_textCtrl5, 0, wx.ALL, 5 )
		gSizer3.Add( bSizerCS30, 1, wx.EXPAND, 5 )

		bSizerCS31 = wx.BoxSizer( wx.HORIZONTAL )
		self.m_staticText8 = wx.StaticText( sbSizerChild.GetStaticBox(), wx.ID_ANY, u"Accurate (h)", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		self.m_textCtrl6 = wx.TextCtrl( sbSizerChild.GetStaticBox(), wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		
		bSizerCS31.Add( self.m_staticText8, 0, wx.ALL, 8 )
		bSizerCS31.Add( self.m_textCtrl6, 0, wx.ALL, 5 )
		gSizer3.Add( bSizerCS31, 1, wx.EXPAND, 5 )

		sbSizerChild.Add( gSizer3, 1, wx.EXPAND, 5 )
		# CS8
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button2 = wx.Button( sbSizerChild.GetStaticBox(), wx.ID_ANY, u"Execute!!!", wx.DefaultPosition, wx.Size( 120,80 ), 0 )
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
		self.m_dirPicker2.Bind( wx.EVT_DIRPICKER_CHANGED, self.set_root_folder )
		self.m_button2.Bind( wx.EVT_BUTTON, self.start_compare )
		# Menu
		self.Bind( wx.EVT_MENU, self.on_guide, id = self.mitGuide.GetId() )
		self.Bind( wx.EVT_MENU, self.on_exit, id = self.mitExit.GetId() )
		self.Bind(wx.EVT_CLOSE, self.on_exit)
		self.Bind( wx.EVT_MENU, self.on_about, id = self.mitAbout.GetId() )
	
	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def set_root_folder( self, event ):
		COMPARE_FOLD = event.GetPath()
		print("---------------")
		print(event.GetPath())
	
	def start_compare( self, event ):
		print("--------?-------")
		print(COMPARE_FOLD)
		for r, d, f in os.walk(COMPARE_FOLD):
		    print(r)
		    print(d)
		    print(f)
		    break

	def on_guide( self, event ):
		nb=NCBox(
			r"""
0. Your folder must structure :

	|-\Root
	|-\Root\Old_Image_Folder

	|-\Root\Old_Image_Folder\FolderToCpx1
	|-\Root\Old_Image_Folder\FolderToCpx1\image1.jpg
	|-\Root\Old_Image_Folder\FolderToCpx1\image2.jpg
	...
	|-\Root\Old_Image_Folder\FolderToCpx2
	|-\Root\Old_Image_Folder\FolderToCpx2\image3.jpg
	|-\Root\Old_Image_Folder\FolderToCpx2\image4.jpg
	...
	|-\Root\New_Image_Folder\FolderToCpx1
	|-\Root\New_Image_Folder\FolderToCpx1\image1.jpg
	|-\Root\New_Image_Folder\FolderToCpx1\image2.jpg
	...
	|-\Root\New_Image_Folder\FolderToCpx2
	|-\Root\New_Image_Folder\FolderToCpx2\image3.jpg
	|-\Root\New_Image_Folder\FolderToCpx2\image4.jpg
	...
	...

1. Step 1: Click Browse to choose your folder.
* Default is : ".\CompareFolder"

2. Step 2: Set ignore point
* IP is ignore point. You must set Top(x,y) and Bottom(x,y) ignore point!	
* Require : Top<Bottom .
	Example : Top(2,5) , Bottom(900,600)

3. Step 3: Set Accurate width(w) and height(h).

4. Step 4: Click Execute. Result in ".\OutFolder"
			""",
			None,
			title="NCIC User Guide",
			style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
		)
		nb.Show()

	def on_exit( self, event ):
		self.Destroy()
		wx.GetApp().ExitMainLoop()
	
	def on_about( self, event ):
		nb=NCBox(
			"""
Name :  NCIC
Version : 1.2
Last release : 20/06/2019
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