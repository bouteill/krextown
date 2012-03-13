#-------------------------------------------------------------------------------
# Name:        jrs01.py
# Purpose:     
#
# Author:      Anung Ariwibowo, barliant@gmail.com
#
# Created:     20120302
# Copyright:   (c) Anung 2012
# Licence:     <your licence>
# version:
# 20120302 Start.
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import wx
import networkx as nx


# SET TO False to suppress Debug information
DBG = True


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, \
                size=(-1,-1))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        fileMenu = wx.Menu()
        menuAbout = fileMenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
        menuOpenFile = fileMenu.Append(wx.ID_OPEN , "&Open", " Open an existing file")
        fileMenu.AppendSeparator()
        menuExit = fileMenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpenFile)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Show(True)


    def OnAbout(self, event):
        # A message dialog box with an OK button.
        dlg = wx.MessageDialog(self, "A small text Editor.", "About Sample Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()


    def OnOpen(self, event):
        import os

        self.dirname = ""
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), "r")
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()


    def OnExit(self, event):
        self.Close(True)


class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # create some sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridBagSizer(hgap=5, vgap=5)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.quote= wx.StaticText(self, label="Your quote:")
        grid.Add(self.quote, pos=(0,0))

        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        self.logger= wx.TextCtrl(self, size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)

        # A button
        self.button= wx.Button(self, label="Save")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)

        # the edit control - one line version
        self.lblName = wx.StaticText(self, label="Your name:")
        grid.Add(self.lblName, pos=(1,0))
        self.editName = wx.TextCtrl(self, value="Enter here your name", size=(140,-1))
        grid.Add(self.editName, pos=(1,1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editName)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editName)

        # the combobox control
        self.sampleList= ['friends', 'advertising', 'web search', 'Yellow Pages']
        self.lblHear = wx.StaticText(self, label="How did you hear from us?")
        grid.Add(self.lblHear, pos=(3,0))
        self.editHear = wx.ComboBox(self, size=(95, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        grid.Add(self.editHear, pos=(3,1))
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.editHear)
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editHear)

        # add a spacer to the sizer
        grid.Add((10,40), pos=(2,0))

        # checkbox
        self.insure = wx.CheckBox(self, label="Do you want Insured Shipment?")
        grid.Add(self.insure, pos=(4,0), span=(1,2), flag=wx.BOTTOM, border=5)
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.insure)

        # radio boxes
        radioList = ['blue', 'red', 'yellow', 'orange', 'green', 'purple', 'navy blue', 'black', 'gray']
        rb = wx.RadioBox(self, label="What color would you like?", pos=(20,210), choices=radioList, majorDimension=3, style=wx.RA_SPECIFY_COLS)
        grid.Add(rb, pos=(5,0), span=(1,2))
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, rb)
        hSizer.Add(grid, 0, wx.ALL, 5)
        hSizer.Add(self.logger)
        mainSizer.Add(hSizer, 0, wx.ALL, 5)
        mainSizer.Add(self.button, 0, wx.CENTER)
        self.SetSizerAndFit(mainSizer)

    def EvtRadioBox(self, event):
        self.logger.AppendText('EvtRadioBox: %d\n' %event.GetInt())

    def EvtComboBox(self, event):
        self.logger.AppendText('EvtComboBox: %s\n' %event.GetString())

    def OnClick(self, event):
        self.logger.AppendText(" Click on object with Id %d\n" %event.GetId())

    def EvtText(self, event):
        self.logger.AppendText("EvtText: %s\n" %event.GetString())

    def EvtChar(self, event):
        self.logger.AppendText("EvtChar: %d\n" %event.GetKeyCode())
        event.Skip()

    def EvtCheckBox(self, event):
        self.logger.AppendText("EvtCheckBox: %d\n" %event.Checked())


def jrs01():
    print("Opening trainingData.csv..")
    train = open('trainingData.csv', 'r')
    print("Opening trainingLabels.txt..")
    label = open('trainingLabels.txt', 'r')
    
    gjrs = nx.Graph()
    
    for lines in train:
        print lines
    
    train.close()
    label.close()
    print("Done..")
    
def main():
    '''
    app = wx.App(False)
    #frm = MainWindow(None, "Simple Editor")
    frm = wx.Frame(None)
    panel = ExamplePanel(frm)
    frm.Show()
    app.MainLoop()
    '''
    jrs01()


if __name__ == '__main__':
    main()
