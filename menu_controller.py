from PyQt5 import QtCore, QtGui, QtWidgets
from menu import Ui_menu
from BeamCal_base import BeamCalButtonClicked
from BeamCal import Ui_BeamCal
from ColumnCal import Ui_ColumnCal
from ColumnCal_base import ColCalButtonClicked
from CnnctDsgn import Ui_CnnctDsgn
from CnnctDsgn_base import CnnctDsgnButtonClicked

class menu_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx
        self.setWindowIcon(QtGui.QIcon('cover.png'))
        # self.setWindowTitle("title")
        self.ui = Ui_menu()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        # TODO
        self.ui.FlexCal.clicked.connect(self.FlexCalClicked)
        self.ui.ColumnCal.clicked.connect(self.ColumnCalClicked)
        self.ui.CnnctDsgn.clicked.connect(self.CnnctDsgnClicked)

    def FlexCalClicked(self):
      self.hide()
      self.ui=w2_controller()
      self.ui.show()

    def ColumnCalClicked(self):
      self.hide()
      self.ui=w3_controller()
      self.ui.show()

    def CnnctDsgnClicked(self):
      self.hide()
      self.ui=w4_controller()
      self.ui.show()


class w2_controller(QtWidgets.QMainWindow,Ui_BeamCal):
  def __init__(self):
    super(w2_controller,self).__init__()
    self.setupUi(self)
    self.setup_control()

  def setup_control(self):
    self.Mux.setText('0')
    self.Vuy.setText('0')
    self.calbutton.clicked.connect(lambda:BeamCalButtonClicked(self))
    self.closeButton1.clicked.connect(self.closebutton1Clicked)

  def closebutton1Clicked(self):
    self.hide()
    self.ui=menu_controller()
    self.ui.show() 

class w3_controller(Ui_ColumnCal,w2_controller,QtWidgets.QMainWindow):
  def __init__(self):
    super(w3_controller,self).__init__()
    self.setupUi(self)
    self.setup_control()

  def setup_control(self):
    self.Pu.setText('0')
    self.Mux.setText('0')
    self.Muy.setText('0')
    self.Vux.setText('0')
    self.Vuy.setText('0')
    self.cft='no'
    self.label_fc.clicked.connect(self.label_fcClicked)
    self.calbutton.clicked.connect(lambda:ColCalButtonClicked(self))
    self.closeButton1.clicked.connect(self.closebutton1Clicked)

  def label_fcClicked(self) :
    self.cft='yes' if self.label_fc.isChecked() else 'no'  
    return self.cft

class w4_controller(Ui_CnnctDsgn,w2_controller,QtWidgets.QMainWindow):
  def __init__(self):
    super(w4_controller,self).__init__()
    self.setupUi(self)
    self.setup_control()

  def setup_control(self):
    self.Mg.setText('0')
    self.Vg.setText('0')
    self.sd='yes'
    self.label_selfdesign.clicked.connect(self.selfdesignClicked)
    self.calbutton.clicked.connect(lambda:CnnctDsgnButtonClicked(self))
    self.closeButton1.clicked.connect(self.closebutton1Clicked)

  def selfdesignClicked(self) :
    self.sd='yes' if self.label_selfdesign.isChecked() else 'no'  
    return self.sd