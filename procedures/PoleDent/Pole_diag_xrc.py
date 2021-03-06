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




class xrcPoleDiag(wx.Dialog):
#!XRCED:begin-block:xrcPoleDiag.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrcPoleDiag.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreDialog()
        self.PreCreate(pre)
        get_resources().LoadOnDialog(pre, parent, "PoleDiag")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.PoleSelectFile = xrc.XRCCTRL(self, "PoleSelectFile")
        self.PoleFile = xrc.XRCCTRL(self, "PoleFile")
        self.IF_EXTEND = xrc.XRCCTRL(self, "IF_EXTEND")
        self.IF_PROCEDURE = xrc.XRCCTRL(self, "IF_PROCEDURE")
        self.SLIDE_DENTPER = xrc.XRCCTRL(self, "SLIDE_DENTPER")
        self.RIGHTEND_XCOORD = xrc.XRCCTRL(self, "RIGHTEND_XCOORD")
        self.LEFTEND_XCOORD = xrc.XRCCTRL(self, "LEFTEND_XCOORD")
        self.LENGTH_INCR = xrc.XRCCTRL(self, "LENGTH_INCR")
        self.CHECK_MONPROC = xrc.XRCCTRL(self, "CHECK_MONPROC")
        self.CHECK_BENDPROC = xrc.XRCCTRL(self, "CHECK_BENDPROC")
        self.PARA_leftsupportx = xrc.XRCCTRL(self, "PARA_leftsupportx")
        self.PARA_rightsupportx = xrc.XRCCTRL(self, "PARA_rightsupportx")
        self.PARA_supporty = xrc.XRCCTRL(self, "PARA_supporty")
        self.PARA_leftplatecenterx = xrc.XRCCTRL(self, "PARA_leftplatecenterx")
        self.PARA_rightplatecenterx = xrc.XRCCTRL(self, "PARA_rightplatecenterx")
        self.PARA_plateheighty = xrc.XRCCTRL(self, "PARA_plateheighty")
        self.PARA_lengthx = xrc.XRCCTRL(self, "PARA_lengthx")
        self.PARA_heighty = xrc.XRCCTRL(self, "PARA_heighty")
        self.PARA_stiffness = xrc.XRCCTRL(self, "PARA_stiffness")
        self.PoleProcess = xrc.XRCCTRL(self, "PoleProcess")





# ------------------------ Resource data ----------------------

def __init_resources():
    global __res
    __res = xrc.EmptyXmlResource()

    wx.FileSystem.AddHandler(wx.MemoryFSHandler())

    Pole_diag_xrc = '''\
<?xml version="1.0" ?><resource>
  <object class="wxDialog" name="PoleDiag">
    <title>Pole Pre-Process </title>
    <style>wxDEFAULT_DIALOG_STYLE|wxCAPTION|wxSYSTEM_MENU</style>
    <object class="wxBoxSizer">
      <orient>wxVERTICAL</orient>
      <object class="sizeritem">
        <object class="wxBoxSizer">
          <orient>wxVERTICAL</orient>
          <object class="sizeritem">
            <object class="wxStaticBoxSizer">
              <label>Input File</label>
              <orient>wxVERTICAL</orient>
              <object class="sizeritem">
                <object class="wxFlexGridSizer">
                  <cols>2</cols>
                  <object class="sizeritem">
                    <object class="wxStaticText">
                      <label>Select the Marc *.dat File</label>
                    </object>
                    <flag>wxALL|wxEXPAND</flag>
                  </object>
                  <rows>2</rows>
                  <vgap>11</vgap>
                  <hgap>5</hgap>
                  <growablecols>1</growablecols>
                  <object class="sizeritem">
                    <object class="wxButton" name="PoleSelectFile">
                      <style/>
                      <label>Browser..</label>
                    </object>
                  </object>
                  <object class="spacer">
                    <size>0,0</size>
                  </object>
                </object>
              </object>
              <object class="sizeritem">
                <object class="wxTextCtrl" name="PoleFile"/>
                <flag>wxALL|wxEXPAND</flag>
              </object>
              <object class="spacer">
                <size>20,20</size>
              </object>
              <object class="sizeritem">
                <object class="wxCheckBox" name="IF_EXTEND">
                  <label>Extend Ends</label>
                </object>
              </object>
              <object class="spacer">
                <size>10,10</size>
              </object>
              <object class="sizeritem">
                <object class="wxCheckBox" name="IF_PROCEDURE">
                  <label>Create Procedure</label>
                </object>
              </object>
            </object>
            <flag>wxALL|wxEXPAND</flag>
          </object>
          <object class="spacer">
            <size>20,20</size>
          </object>
          <object class="sizeritem">
            <object class="wxStaticBoxSizer">
              <label>Dent Material Option</label>
              <orient>wxVERTICAL</orient>
              <object class="sizeritem">
                <object class="wxFlexGridSizer">
                  <cols>2</cols>
                  <object class="sizeritem">
                    <object class="wxStaticText">
                      <label>Dent Material Percentage</label>
                    </object>
                    <flag>wxALL|wxEXPAND|wxALIGN_CENTRE_VERTICAL|wxALIGN_CENTRE_HORIZONTAL</flag>
                  </object>
                  <vgap>11</vgap>
                  <hgap>5</hgap>
                  <growablecols>1</growablecols>
                  <object class="sizeritem">
                    <object class="wxSlider" name="SLIDE_DENTPER">
                      <value>50</value>
                      <min/>
                      <max>100</max>
                      <style>wxSL_HORIZONTAL|wxSL_AUTOTICKS|wxSL_LABELS</style>
                      <tickfreq>20</tickfreq>
                    </object>
                  </object>
                </object>
                <flag>wxALL|wxEXPAND|wxALIGN_CENTRE_VERTICAL</flag>
              </object>
            </object>
            <option>1</option>
            <flag>wxALL|wxEXPAND</flag>
          </object>
          <object class="spacer">
            <size>20,20</size>
          </object>
          <object class="sizeritem">
            <object class="wxStaticBoxSizer">
              <label>Side Extension</label>
              <orient>wxVERTICAL</orient>
              <object class="sizeritem">
                <object class="wxGridSizer">
                  <cols>2</cols>
                  <rows>3</rows>
                  <object class="sizeritem">
                    <object class="wxStaticText">
                      <label>surface_rightend (+)</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <object class="wxTextCtrl" name="RIGHTEND_XCOORD"/>
                  </object>
                  <object class="sizeritem">
                    <object class="wxStaticText">
                      <label>surface_leftend    (-)</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <object class="wxTextCtrl" name="LEFTEND_XCOORD"/>
                  </object>
                  <vgap>5</vgap>
                  <hgap>5</hgap>
                  <object class="sizeritem">
                    <object class="wxStaticText">
                      <label>Increment Length</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <object class="wxTextCtrl" name="LENGTH_INCR"/>
                  </object>
                </object>
              </object>
            </object>
            <flag>wxEXPAND</flag>
          </object>
          <object class="spacer">
            <size>20,20</size>
          </object>
          <object class="sizeritem">
            <object class="wxStaticBoxSizer">
              <label>Procedure Option</label>
              <orient>wxVERTICAL</orient>
              <object class="sizeritem">
                <object class="wxFlexGridSizer">
                  <cols>2</cols>
                  <rows>2</rows>
                  <vgap>11</vgap>
                  <hgap>5</hgap>
                  <growablecols>1</growablecols>
                  <object class="sizeritem">
                    <object class="wxStaticText">
                      <label>Genrate Pure Bending</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <object class="wxRadioButton" name="CHECK_MONPROC">
                      <label/>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <object class="wxStaticText">
                      <label>Generate four point bending</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <object class="wxRadioButton" name="CHECK_BENDPROC">
                      <label/>
                    </object>
                  </object>
                </object>
                <flag>wxALL|wxEXPAND|wxALIGN_CENTRE_VERTICAL|wxALIGN_CENTRE_HORIZONTAL</flag>
              </object>
            </object>
            <flag>wxEXPAND</flag>
          </object>
          <object class="spacer">
            <size>20,20</size>
          </object>
          <object class="sizeritem">
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <object class="wxStaticBoxSizer">
                  <label>Support Plate</label>
                  <orient>wxVERTICAL</orient>
                  <object class="sizeritem">
                    <object class="wxGridSizer">
                      <cols>2</cols>
                      <rows>3</rows>
                      <object class="sizeritem">
                        <object class="wxStaticText">
                          <label>left Support X</label>
                        </object>
                      </object>
                      <object class="sizeritem">
                        <object class="wxTextCtrl" name="PARA_leftsupportx"/>
                      </object>
                      <object class="sizeritem">
                        <object class="wxStaticText">
                          <label>right Support X</label>
                        </object>
                      </object>
                      <object class="sizeritem">
                        <object class="wxTextCtrl" name="PARA_rightsupportx"/>
                      </object>
                      <object class="sizeritem">
                        <object class="wxStaticText">
                          <label>Support Y</label>
                        </object>
                      </object>
                      <object class="sizeritem">
                        <object class="wxTextCtrl" name="PARA_supporty"/>
                      </object>
                      <vgap>5</vgap>
                      <hgap>5</hgap>
                    </object>
                  </object>
                </object>
                <flag>wxEXPAND</flag>
              </object>
              <object class="sizeritem">
                <object class="wxStaticBoxSizer">
                  <label>Loading Plate</label>
                  <orient>wxVERTICAL</orient>
                  <object class="sizeritem">
                    <object class="wxGridSizer">
                      <cols>2</cols>
                      <rows>6</rows>
                      <object class="sizeritem">
                        <object class="wxStaticText">
                          <label>left load  X</label>
                        </object>
                      </object>
                      <object class="sizeritem">
                        <object class="wxTextCtrl" name="PARA_leftplatecenterx"/>
                      </object>
                      <object class="sizeritem">
                        <object class="wxStaticText">
                          <label>right load X</label>
                        </object>
                      </object>
                      <object class="sizeritem">
                        <object class="wxTextCtrl" name="PARA_rightplatecenterx"/>
                      </object>
                      <object class="sizeritem">
                        <object class="wxStaticText">
                          <label>Load range Y</label>
                        </object>
                      </object>
                      <object class="sizeritem">
                        <object class="wxTextCtrl" name="PARA_plateheighty"/>
                      </object>
                      <object class="sizeritem">
                        <object class="wxStaticText">
                          <label>Plate length (x)</label>
                        </object>
                      </object>
                      <object class="sizeritem">
                        <object class="wxTextCtrl" name="PARA_lengthx"/>
                      </object>
                      <vgap>5</vgap>
                      <hgap>5</hgap>
                      <object class="sizeritem">
                        <object class="wxStaticText">
                          <label>Plate height y</label>
                        </object>
                      </object>
                      <object class="sizeritem">
                        <object class="wxTextCtrl" name="PARA_heighty"/>
                      </object>
                      <object class="sizeritem">
                        <object class="wxStaticText">
                          <label>spring stiffness</label>
                        </object>
                      </object>
                      <object class="sizeritem">
                        <object class="wxTextCtrl" name="PARA_stiffness"/>
                      </object>
                    </object>
                  </object>
                </object>
                <flag>wxEXPAND</flag>
              </object>
            </object>
          </object>
          <object class="spacer">
            <size>20,20</size>
          </object>
          <object class="sizeritem">
            <object class="wxBoxSizer">
              <orient>wxHORIZONTAL</orient>
              <object class="sizeritem">
                <object class="wxGridSizer">
                  <cols>2</cols>
                  <rows>1</rows>
                  <hgap>5</hgap>
                  <object class="sizeritem">
                    <object class="wxButton">
                      <label>Help</label>
                    </object>
                  </object>
                  <object class="sizeritem">
                    <object class="wxButton" name="PoleProcess">
                      <label>Process</label>
                    </object>
                  </object>
                </object>
              </object>
            </object>
            <flag>wxALIGN_RIGHT</flag>
          </object>
        </object>
        <option>1</option>
        <flag>wxALL|wxEXPAND</flag>
        <border>10</border>
      </object>
    </object>
  </object>
</resource>'''

    wx.MemoryFSHandler.AddFile('XRC/Pole_diag/Pole_diag_xrc', Pole_diag_xrc)
    __res.Load('memory:XRC/Pole_diag/Pole_diag_xrc')

