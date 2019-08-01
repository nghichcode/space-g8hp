# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui

###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.m_mgr = wx.aui.AuiManager()
        self.m_mgr.SetManagedWindow( self )
        self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)
        
        self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        self.m_mgr.AddPane( self.m_filePicker1, wx.aui.AuiPaneInfo() .Left() .CloseButton( False ).PinButton( True ).PaneBorder( False ).Float().FloatingPosition( wx.Point( 458,250 ) ).Resizable().FloatingSize( wx.Size( 219,65 ) ).Floatable( False ) )

        self.m_mgr.Update()
        self.Centre( wx.BOTH )
    
    def __del__( self ):
        self.m_mgr.UnInit()

if __name__ == '__main__':
    app = wx.App()
    mf = MyFrame3(None)
    mf.Show()
    app.MainLoop()