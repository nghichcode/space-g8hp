# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:26:52 2019

@author: Win 8.1 Version 2
"""

import wx
import wx.xrc

class MyFrame1 ( wx.Frame ):
	
#	def __init__( self, parent ):
#		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
	def __init__(self, *args, **kw):
		super(MyFrame1, self).__init__(*args, **kw)
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer28 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		bSizer28.Add( self.m_button3, 0, wx.ALIGN_RIGHT, 0 )
		
		
		bSizer5.Add( bSizer28, 1, wx.EXPAND, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.VERTICAL )
		
		bSizer101 = wx.BoxSizer( wx.VERTICAL )
		
		
#		bSizer101.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
#        bSizer101.Add( 1,0,0 )
#        bSizer101.Add( 1,0,1 )
		
		
		sbSizer1.Add( bSizer101, 1, wx.EXPAND, 5 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer1.Add( self.m_staticText2, 0, wx.ALL, 8 )
		
		self.m_textCtrl1 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		
		gSizer1.Add( bSizer1, 1, wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText21 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		bSizer11.Add( self.m_staticText21, 0, wx.ALL, 8 )
		
		self.m_textCtrl11 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_textCtrl11, 0, wx.ALL, 5 )
		
		
		gSizer1.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		
		sbSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		gSizer11 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText22 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		bSizer12.Add( self.m_staticText22, 0, wx.ALL, 8 )
		
		self.m_textCtrl12 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_textCtrl12, 0, wx.ALL, 5 )
		
		
		gSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )
		
		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText211 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )
		bSizer111.Add( self.m_staticText211, 0, wx.ALL, 8 )
		
		self.m_textCtrl111 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer111.Add( self.m_textCtrl111, 0, wx.ALL, 5 )
		
		
		gSizer11.Add( bSizer111, 1, wx.EXPAND, 5 )
		
		
		sbSizer1.Add( gSizer11, 1, wx.EXPAND, 5 )
		
		gSizer111 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer121 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText221 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )
		bSizer121.Add( self.m_staticText221, 0, wx.ALL, 8 )
		
		self.m_textCtrl121 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer121.Add( self.m_textCtrl121, 0, wx.ALL, 5 )
		
		
		gSizer111.Add( bSizer121, 1, wx.EXPAND, 5 )
		
		bSizer1111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2111 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText2111.Wrap( -1 )
		bSizer1111.Add( self.m_staticText2111, 0, wx.ALL, 8 )
		
		self.m_textCtrl1111 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1111.Add( self.m_textCtrl1111, 0, wx.ALL, 5 )
		
		
		gSizer111.Add( bSizer1111, 1, wx.EXPAND, 5 )
		
		
		sbSizer1.Add( gSizer111, 1, wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		
#		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
#		bSizer10.Add( 1,0,1 )
		
		
		sbSizer1.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button2 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Execute!!!", wx.DefaultPosition, wx.Size( 120,80 ), 0 )
		self.m_button2.SetFont( wx.Font( 16, 70, 90, 92, False, wx.EmptyString ) )
		self.m_button2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		bSizer9.Add( self.m_button2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer1.Add( bSizer9, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer5.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )
			
if __name__ == '__main__':
    app = wx.App()
    fr= MyFrame1(None, title='heio',
         style = 0  )
    fr.Show()
#    frm = HelloFrame(None, title='Hello World 2')
#    frm.Show()
    app.MainLoop()
