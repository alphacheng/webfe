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




class xrcDIAG_Section(wx.Frame):
#!XRCED:begin-block:xrcDIAG_Section.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrcDIAG_Section.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreFrame()
        self.PreCreate(pre)
        get_resources().LoadOnFrame(pre, parent, "DIAG_Section")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.REC_NAME = xrc.XRCCTRL(self, "REC_NAME")
        self.REC_WIDTH = xrc.XRCCTRL(self, "REC_WIDTH")
        self.REC_HEIGHT = xrc.XRCCTRL(self, "REC_HEIGHT")
        self.REC_HEIGHTSEG = xrc.XRCCTRL(self, "REC_HEIGHTSEG")
        self.REC_REINF = xrc.XRCCTRL(self, "REC_REINF")
        self.REC_APP = xrc.XRCCTRL(self, "REC_APP")
        self.CIRC_NAME = xrc.XRCCTRL(self, "CIRC_NAME")
        self.CIRC_RAD = xrc.XRCCTRL(self, "CIRC_RAD")
        self.CIRC_SEG = xrc.XRCCTRL(self, "CIRC_SEG")
        self.CIRC_REINF = xrc.XRCCTRL(self, "CIRC_REINF")
        self.CIRCAPP = xrc.XRCCTRL(self, "CIRCAPP")
        self.T_Name = xrc.XRCCTRL(self, "T_Name")
        self.T_H = xrc.XRCCTRL(self, "T_H")
        self.T_BF = xrc.XRCCTRL(self, "T_BF")
        self.T_TF = xrc.XRCCTRL(self, "T_TF")
        self.T_TF1 = xrc.XRCCTRL(self, "T_TF1")
        self.T_WF = xrc.XRCCTRL(self, "T_WF")
        self.T_TW = xrc.XRCCTRL(self, "T_TW")
        self.T_HW = xrc.XRCCTRL(self, "T_HW")
        self.T_REINF = xrc.XRCCTRL(self, "T_REINF")
        self.T_APP = xrc.XRCCTRL(self, "T_APP")





# ------------------------ Resource data ----------------------

def __init_resources():
    global __res
    __res = xrc.EmptyXmlResource()

    wx.FileSystem.AddHandler(wx.MemoryFSHandler())

    section_xrc = '''\
<?xml version="1.0" ?><resource>
  <object class="wxFrame" name="DIAG_Section">
    <title>Section Create</title>
    <object class="wxPanel">
      <object class="wxBoxSizer">
        <orient>wxVERTICAL</orient>
        <object class="sizeritem">
          <object class="wxBoxSizer">
            <orient>wxVERTICAL</orient>
            <object class="sizeritem">
              <object class="wxNotebook">
                <object class="notebookpage">
                  <label>Shape Section</label>
                  <object class="wxPanel">
                    <object class="wxBoxSizer">
                      <orient>wxVERTICAL</orient>
                      <object class="sizeritem">
                        <object class="wxStaticBoxSizer">
                          <label>Rectangle</label>
                          <orient>wxVERTICAL</orient>
                          <object class="sizeritem">
                            <object class="wxGridSizer">
                              <cols>2</cols>
                              <rows>2</rows>
                              <object class="sizeritem">
                                <object class="wxStaticText" name="">
                                  <label>Name</label>
                                </object>
                              </object>
                              <object class="sizeritem">
                                <object class="wxTextCtrl" name="REC_NAME"/>
                              </object>
                              <object class="sizeritem">
                                <object class="wxStaticText" name="">
                                  <label>width</label>
                                </object>
                              </object>
                              <object class="sizeritem">
                                <object class="wxTextCtrl" name="REC_WIDTH"/>
                              </object>
                              <object class="sizeritem">
                                <object class="wxStaticText" name="">
                                  <label>Height</label>
                                </object>
                              </object>
                              <object class="sizeritem">
                                <object class="wxTextCtrl" name="REC_HEIGHT"/>
                              </object>
                              <object class="sizeritem">
                                <object class="wxStaticText" name="">
                                  <label>Segments of Height</label>
                                </object>
                              </object>
                              <object class="sizeritem">
                                <object class="wxTextCtrl" name="REC_HEIGHTSEG"/>
                              </object>
                              <object class="sizeritem">
                                <object class="wxStaticText">
                                  <label>Reinforcement</label>
                                </object>
                              </object>
                              <object class="sizeritem">
                                <object class="wxChoice" name="REC_REINF">
                                  <content/>
                                </object>
                              </object>
                              <object class="spacer">
                                <size>0,0</size>
                              </object>
                              <vgap>2</vgap>
                              <hgap>2</hgap>
                            </object>
                            <border>5</border>
                          </object>
                          <object class="sizeritem">
                            <object class="wxGridSizer">
                              <cols>1</cols>
                              <rows>1</rows>
                              <object class="sizeritem">
                                <object class="wxButton" name="REC_APP">
                                  <label>Apply</label>
                                  <style/>
                                </object>
                              </object>
                            </object>
                            <flag>wxALIGN_RIGHT</flag>
                            <border>3</border>
                          </object>
                        </object>
                        <option>1</option>
                        <flag>wxALL|wxEXPAND</flag>
                      </object>
                      <object class="sizeritem">
                        <object class="wxStaticBoxSizer">
                          <label>Circular</label>
                          <orient>wxVERTICAL</orient>
                          <object class="sizeritem">
                            <object class="wxGridSizer">
                              <cols>2</cols>
                              <rows>2</rows>
                              <object class="sizeritem">
                                <object class="wxStaticText" name="">
                                  <label>Name</label>
                                </object>
                              </object>
                              <object class="sizeritem">
                                <object class="wxTextCtrl" name="CIRC_NAME"/>
                              </object>
                              <object class="sizeritem">
                                <object class="wxStaticText" name="">
                                  <label>Radius</label>
                                </object>
                              </object>
                              <object class="sizeritem">
                                <object class="wxTextCtrl" name="CIRC_RAD"/>
                              </object>
                              <object class="sizeritem">
                                <object class="wxStaticText" name="">
                                  <label>Segments of Height</label>
                                </object>
                              </object>
                              <object class="sizeritem">
                                <object class="wxTextCtrl" name="CIRC_SEG"/>
                              </object>
                              <object class="sizeritem">
                                <object class="wxStaticText">
                                  <label>Reinforcement</label>
                                </object>
                              </object>
                              <object class="sizeritem">
                                <object class="wxChoice" name="CIRC_REINF">
                                  <content/>
                                </object>
                              </object>
                              <object class="spacer">
                                <size>0,0</size>
                              </object>
                            </object>
                            <border>5</border>
                          </object>
                          <object class="sizeritem">
                            <object class="wxGridSizer">
                              <cols>1</cols>
                              <rows>1</rows>
                              <object class="sizeritem">
                                <object class="wxButton" name="CIRCAPP">
                                  <label>Apply</label>
                                  <style/>
                                </object>
                              </object>
                            </object>
                            <flag>wxALIGN_RIGHT</flag>
                            <border>3</border>
                          </object>
                        </object>
                        <option>1</option>
                        <flag>wxALL|wxEXPAND</flag>
                      </object>
                    </object>
                  </object>
                </object>
                <object class="notebookpage">
                  <label>T Section</label>
                  <object class="wxPanel">
                    <object class="wxBoxSizer">
                      <orient>wxVERTICAL</orient>
                      <object class="sizeritem">
                        <object class="wxGridSizer">
                          <cols>2</cols>
                          <rows>2</rows>
                          <object class="spacer">
                            <size>0,0</size>
                          </object>
                          <object class="spacer">
                            <size>0,0</size>
                          </object>
                          <object class="sizeritem">
                            <object class="wxStaticText">
                              <label>Name</label>
                            </object>
                          </object>
                          <object class="sizeritem">
                            <object class="wxTextCtrl" name="T_Name"/>
                          </object>
                          <object class="sizeritem">
                            <object class="wxStaticText">
                              <label>Total Height</label>
                            </object>
                          </object>
                          <object class="sizeritem">
                            <object class="wxTextCtrl" name="T_H"/>
                          </object>
                          <object class="sizeritem">
                            <object class="wxStaticText">
                              <label>Width of top flange</label>
                            </object>
                          </object>
                          <object class="sizeritem">
                            <object class="wxTextCtrl" name="T_BF"/>
                          </object>
                          <object class="sizeritem">
                            <object class="wxStaticText">
                              <label>Total thickness of flange</label>
                            </object>
                          </object>
                          <object class="sizeritem">
                            <object class="wxTextCtrl" name="T_TF"/>
                          </object>
                          <object class="sizeritem">
                            <object class="wxStaticText">
                              <label>thickness if taper portion</label>
                            </object>
                          </object>
                          <object class="sizeritem">
                            <object class="wxTextCtrl" name="T_TF1"/>
                          </object>
                          <object class="sizeritem">
                            <object class="wxStaticText">
                              <label>top width of taper</label>
                            </object>
                          </object>
                          <object class="sizeritem">
                            <object class="wxTextCtrl" name="T_WF"/>
                          </object>
                          <object class="sizeritem">
                            <object class="wxStaticText">
                              <label>width of web</label>
                            </object>
                          </object>
                          <object class="sizeritem">
                            <object class="wxTextCtrl" name="T_TW"/>
                          </object>
                          <object class="sizeritem">
                            <object class="wxStaticText">
                              <label>height of web</label>
                            </object>
                          </object>
                          <object class="sizeritem">
                            <object class="wxTextCtrl" name="T_HW">
                              <style/>
                            </object>
                          </object>
                          <object class="sizeritem">
                            <object class="wxStaticText">
                              <label>Reinforcement</label>
                            </object>
                          </object>
                          <object class="sizeritem">
                            <object class="wxChoice" name="T_REINF">
                              <content/>
                            </object>
                          </object>
                          <vgap>2</vgap>
                          <hgap>2</hgap>
                          <object class="spacer">
                            <size>0,0</size>
                          </object>
                        </object>
                        <border>5</border>
                      </object>
                      <object class="sizeritem">
                        <object class="wxGridSizer">
                          <cols>1</cols>
                          <rows>1</rows>
                          <object class="sizeritem">
                            <object class="wxButton" name="T_APP">
                              <label>Apply</label>
                            </object>
                          </object>
                        </object>
                        <flag>wxALIGN_RIGHT</flag>
                      </object>
                    </object>
                  </object>
                </object>
              </object>
              <option>1</option>
              <flag>wxALL|wxEXPAND</flag>
            </object>
          </object>
          <option>1</option>
          <flag>wxALL|wxEXPAND</flag>
        </object>
      </object>
    </object>
    <centered>1</centered>
    <size>300,500</size>
    <style>wxDEFAULT_DIALOG_STYLE</style>
  </object>
</resource>'''

    wx.MemoryFSHandler.AddFile('XRC/section/section_xrc', section_xrc)
    __res.Load('memory:XRC/section/section_xrc')

