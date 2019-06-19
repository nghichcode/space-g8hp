# -*- coding: utf-8 -*- 
import wx
import wx.xrc
import wx.aui

class NcImageCheck ( wx.Frame ):
	
	# def __init__( self, parent ):
	# 	wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = 0|wx.TAB_TRAVERSAL )
	def __init__(self, *args, **kw):
		super(NcImageCheck, self).__init__(*args, **kw)

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		# self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu2 = wx.Menu()
		self.m_menuItem1a = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Guide", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendSeparator()
		self.m_menuItem1b = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		# self.m_menu2.AppendItem( self.m_menuItem1 )
		self.m_menu2.Append( self.m_menuItem1a )
		self.m_menu2.Append( self.m_menuItem1b )
		
		self.m_menubar1.Append( self.m_menu2, u"File" ) 
		
		self.m_menu3 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		# self.m_menu3.AppendItem( self.m_menuItem2 )
		self.m_menu3.Append( self.m_menuItem2 )
		
		self.m_menubar1.Append( self.m_menu3, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.VERTICAL )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		# bSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		sbSizer1.Add( bSizer1, 1, wx.EXPAND, 5 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"      Top IP(x)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer1.Add( self.m_staticText2, 0, wx.ALL, 8 )
		
		self.m_textCtrl1 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

		gSizer1.Add( bSizer1, 1, wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText21 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"      Top IP(y)", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		bSizer11.Add( self.m_staticText21, 0, wx.ALL, 8 )
		
		self.m_textCtrl11 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_textCtrl11, 0, wx.ALL, 5 )

		gSizer1.Add( bSizer11, 1, wx.EXPAND, 5 )

		sbSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText22 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Bottom IP(x)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		bSizer12.Add( self.m_staticText22, 0, wx.ALL, 8 )
		
		self.m_textCtrl12 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_textCtrl12, 0, wx.ALL, 5 )

		gSizer2.Add( bSizer12, 1, wx.EXPAND, 5 )
		
		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText211 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Bottom IP(y)", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )
		bSizer111.Add( self.m_staticText211, 0, wx.ALL, 8 )
		
		self.m_textCtrl111 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer111.Add( self.m_textCtrl111, 0, wx.ALL, 5 )

		gSizer2.Add( bSizer111, 1, wx.EXPAND, 5 )

		sbSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer121 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText221 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Accurate (w)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )
		bSizer121.Add( self.m_staticText221, 0, wx.ALL, 8 )
		
		self.m_textCtrl121 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer121.Add( self.m_textCtrl121, 0, wx.ALL, 5 )

		gSizer3.Add( bSizer121, 1, wx.EXPAND, 5 )
		
		bSizer1111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2111 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Accurate (h)", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText2111.Wrap( -1 )
		bSizer1111.Add( self.m_staticText2111, 0, wx.ALL, 8 )
		
		self.m_textCtrl1111 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1111.Add( self.m_textCtrl1111, 0, wx.ALL, 5 )

		gSizer3.Add( bSizer1111, 1, wx.EXPAND, 5 )

		sbSizer1.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		# bSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		sbSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button2 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Execute!!!", wx.DefaultPosition, wx.Size( 120,80 ), 0 )
		self.m_button2.SetFont( wx.Font( 16, 70, 90, 92, False, wx.EmptyString ) )
		self.m_button2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		bSizer3.Add( self.m_button2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		sbSizer1.Add( bSizer3, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer5.Add( sbSizer1, 1, wx.EXPAND, 5 )

		self.SetSizer( bSizer5 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar()
		# self.m_statusBar1.SetHelpText( u"Welcome to nc" )
		self.SetStatusText("Welcome to NC Image Check!")

		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass


if __name__ == '__main__':
	app = wx.App()
	nic = NcImageCheck(None, title='NC Image Check', size = wx.Size( 500,300 ), style = 0|wx.TAB_TRAVERSAL)
	nic.Show()
	app.MainLoop()