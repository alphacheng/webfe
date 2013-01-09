# This file was automatically generated by pywxrc.
# -*- coding: UTF-8 -*-

import wx
from wx.lib.pubsub import setuparg1
from wx.lib.pubsub import pub
from  figurecreate_xrc import xrcDIALOG1


class figurecreate(xrcDIALOG1):
    def __init__(self,parent):
        super(figurecreate, self).__init__(parent)
        #self.results = results
        self.FIGURE_OK.Bind(wx.EVT_LEFT_DOWN,self.OnApply)
        
    def update(self,results):
        
        self.FIGURE_PLOTDATASTYLE.Clear()
        self.FIGURE_PLOTDATASTYLE.AppendItems(results.sdb.keys())

        self.FIGURE_PLOTDATAKEY.Clear()
        self.FIGURE_PLOTDATAKEY.AppendItems(results.pdb.keys())
        
    
    def OnApply(self,event):
        fkey = self.FIGURE_KEY.GetValue()
        style = self.FIGURE_PLOTDATASTYLE.GetStringSelection()
        pdata = self.FIGURE_PLOTDATAKEY.GetStringSelection()
        ptype = self.FIGURE_PLOTDATATYPE.GetStringSelection()
        pub.sendMessage("COMMAND", '*plot_figure_add,%s,%s,%s,%s' % (fkey,pdata,style,ptype))
        
        