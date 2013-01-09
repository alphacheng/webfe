# This file was automatically generated by pywxrc.
# -*- coding: UTF-8 -*-

import wx
import wx.xrc as xrc

__res = None

def get_resources():
    """ This function provides access to the XML resources in this module."""
    global __res
    if __res == None:
        __init_resources()
    return __res




class xrc2DPatch(wx.Dialog):
#!XRCED:begin-block:xrc2DPatch.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrc2DPatch.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreDialog()
        self.PreCreate(pre)
        get_resources().LoadOnDialog(pre, parent, "2DPatch")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.PATCH_1D_X0 = xrc.XRCCTRL(self, "PATCH_1D_X0")
        self.PATCH_1D_Y0 = xrc.XRCCTRL(self, "PATCH_1D_Y0")
        self.PATCH_1D_Z0 = xrc.XRCCTRL(self, "PATCH_1D_Z0")
        self.PATCH_1D_X1 = xrc.XRCCTRL(self, "PATCH_1D_X1")
        self.PATCH_1D_Y1 = xrc.XRCCTRL(self, "PATCH_1D_Y1")
        self.PATCH_1D_Z1 = xrc.XRCCTRL(self, "PATCH_1D_Z1")
        self.PATCH_1D_N = xrc.XRCCTRL(self, "PATCH_1D_N")
        self.BTN_APPLY_Line = xrc.XRCCTRL(self, "BTN_APPLY_Line")
        self.PATCH_CYL_X0 = xrc.XRCCTRL(self, "PATCH_CYL_X0")
        self.PATCH_CYL_Y0 = xrc.XRCCTRL(self, "PATCH_CYL_Y0")
        self.PATCH_CYL_Z0 = xrc.XRCCTRL(self, "PATCH_CYL_Z0")
        self.PATCH_CYL_R0 = xrc.XRCCTRL(self, "PATCH_CYL_R0")
        self.PATCH_CYL_R1 = xrc.XRCCTRL(self, "PATCH_CYL_R1")
        self.PATCH_CYL_L = xrc.XRCCTRL(self, "PATCH_CYL_L")
        self.PATCH_CYL_NF = xrc.XRCCTRL(self, "PATCH_CYL_NF")
        self.PATCH_CYL_NZ = xrc.XRCCTRL(self, "PATCH_CYL_NZ")
        self.BTN_APPLY_CYL = xrc.XRCCTRL(self, "BTN_APPLY_CYL")





# ------------------------ Resource data ----------------------

def __init_resources():
    global __res
    __res = xrc.EmptyXmlResource()

    wx.FileSystem.AddHandler(wx.MemoryFSHandler())

    patch_xrc = '''\
<?xml version="1.0" ?><resource>
  <object class="wxDialog" name="2DPatch">
    <title>Create 2D Patch</title>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <object class="wxStaticBoxSizer">
          <label>Straight Lines</label>
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <object class="wxGridSizer">
              <cols>4</cols>
              <rows>2</rows>
              <object class="sizeritem">
                <object class="wxStaticText">
                  <label>Component</label>
                  <style>wxALIGN_CENTRE</style>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxStaticText">
                  <label>X</label>
                  <style>wxALIGN_CENTRE</style>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxStaticText">
                  <label>Y</label>
                  <style>wxALIGN_CENTRE</style>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxStaticText">
                  <label>Z</label>
                  <style>wxALIGN_CENTRE</style>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxStaticText">
                  <label>Start Coordinate</label>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxTextCtrl" name="PATCH_1D_X0"/>
              </object>
              <object class="sizeritem">
                <object class="wxTextCtrl" name="PATCH_1D_Y0"/>
              </object>
              <object class="sizeritem">
                <object class="wxTextCtrl" name="PATCH_1D_Z0"/>
              </object>
              <object class="sizeritem">
                <object class="wxStaticText">
                  <label>End   Coordinate</label>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxTextCtrl" name="PATCH_1D_X1"/>
              </object>
              <object class="sizeritem">
                <object class="wxTextCtrl" name="PATCH_1D_Y1"/>
              </object>
              <object class="sizeritem">
                <object class="wxTextCtrl" name="PATCH_1D_Z1"/>
              </object>
              <object class="sizeritem">
                <object class="wxStaticText">
                  <label>Number of Segment</label>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxTextCtrl" name="PATCH_1D_N"/>
              </object>
              <vgap>5</vgap>
              <hgap>5</hgap>
            </object>
            <flag>wxALIGN_CENTRE_HORIZONTAL</flag>
          </object>
          <object class="spacer">
            <size>10,10</size>
          </object>
          <object class="sizeritem">
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <object class="wxFlexGridSizer">
                  <cols>1</cols>
                  <rows>1</rows>
                  <object class="sizeritem">
                    <object class="wxButton" name="BTN_APPLY_Line">
                      <label>Apply</label>
                    </object>
                  </object>
                  <vgap>5</vgap>
                  <hgap>5</hgap>
                </object>
              </object>
            </object>
            <flag>wxALIGN_RIGHT</flag>
            <border>5</border>
          </object>
        </object>
      </object>
      <object class="sizeritem">
        <object class="wxStaticBoxSizer">
          <label>Cylinder Surface</label>
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <object class="wxGridSizer">
              <cols>4</cols>
              <rows>2</rows>
              <object class="sizeritem">
                <object class="wxStaticText">
                  <label>Component</label>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxStaticText">
                  <label>X</label>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxStaticText">
                  <label>Y</label>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxStaticText">
                  <label>Z</label>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxStaticText">
                  <label>Left Center</label>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxTextCtrl" name="PATCH_CYL_X0"/>
              </object>
              <object class="sizeritem">
                <object class="wxTextCtrl" name="PATCH_CYL_Y0"/>
              </object>
              <object class="sizeritem">
                <object class="wxTextCtrl" name="PATCH_CYL_Z0"/>
              </object>
              <object class="sizeritem">
                <object class="wxStaticText">
                  <label>Left Radius</label>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxTextCtrl" name="PATCH_CYL_R0"/>
              </object>
              <object class="spacer">
                <size>0,0</size>
              </object>
              <object class="spacer">
                <size>0,0</size>
              </object>
              <object class="sizeritem">
                <object class="wxStaticText">
                  <label>Right Radius</label>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxTextCtrl" name="PATCH_CYL_R1"/>
              </object>
              <object class="spacer">
                <size>0,0</size>
              </object>
              <object class="spacer">
                <size>0,0</size>
              </object>
              <object class="sizeritem">
                <object class="wxStaticText">
                  <label>Length</label>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxTextCtrl" name="PATCH_CYL_L"/>
              </object>
              <object class="spacer">
                <size>0,0</size>
              </object>
              <object class="spacer">
                <size>0,0</size>
              </object>
              <object class="sizeritem">
                <object class="wxStaticText">
                  <label>Segment (radius, Z)</label>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxTextCtrl" name="PATCH_CYL_NF"/>
              </object>
              <object class="sizeritem">
                <object class="wxTextCtrl" name="PATCH_CYL_NZ"/>
              </object>
              <vgap>5</vgap>
              <hgap>5</hgap>
            </object>
            <flag>wxALIGN_CENTRE_HORIZONTAL</flag>
          </object>
          <object class="spacer">
            <size>10,10</size>
          </object>
          <object class="sizeritem">
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <object class="wxFlexGridSizer">
                  <cols>1</cols>
                  <rows>1</rows>
                  <object class="sizeritem">
                    <object class="wxButton" name="BTN_APPLY_CYL">
                      <label>Apply</label>
                    </object>
                  </object>
                  <vgap>5</vgap>
                  <hgap>5</hgap>
                </object>
              </object>
            </object>
            <flag>wxALIGN_RIGHT</flag>
            <border>5</border>
          </object>
        </object>
      </object>
    </object>
  </object>
</resource>'''

    wx.MemoryFSHandler.AddFile('XRC/patch/patch_xrc', patch_xrc)
    __res.Load('memory:XRC/patch/patch_xrc')

