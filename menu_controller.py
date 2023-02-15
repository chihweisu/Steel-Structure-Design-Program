from PyQt5 import QtCore, QtGui, QtWidgets
from ui_menu import Ui_Menu
from beamcal_base import beamcal_button_clicked
from ui_beamcal import Ui_BeamCal
from ui_columncal import Ui_ColumnCal
from columncal_base import columncal_button_clicked
from ui_cnnctdsgn import Ui_CnnctDsgn
from cnnctdsgn_base import cnnctdsgn_button_clicked

class MenuController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx
        self.setWindowIcon(QtGui.QIcon('cover.png'))
        # self.setWindowTitle("title")
        self.ui = Ui_Menu()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        # TODO
        self.ui.FlexCal.clicked.connect(self.flexcal_clicked)
        self.ui.ColumnCal.clicked.connect(self.columncal_clicked)
        self.ui.CnnctDsgn.clicked.connect(self.cnnctdsgn_clicked)

    def flexcal_clicked(self):
      self.hide()
      self.ui=W2Controller()
      self.ui.show()

    def columncal_clicked(self):
      self.hide()
      self.ui=W3Controller()
      self.ui.show()

    def cnnctdsgn_clicked(self):
      self.hide()
      self.ui=W4Controller()
      self.ui.show()


class W2Controller(QtWidgets.QMainWindow,Ui_BeamCal):
  def __init__(self):
    super(W2Controller,self).__init__()
    self.setupUi(self)
    self.setup_control()

  def setup_control(self):
    self.Mux.setText('0')
    self.Vuy.setText('0')
    self.calbutton.clicked.connect(lambda:beamcal_button_clicked(self))
    self.closeButton1.clicked.connect(self.closebutton1Clicked)

  def closebutton1Clicked(self):
    self.hide()
    self.ui=MenuController()
    self.ui.show() 

class W3Controller(Ui_ColumnCal,W2Controller,QtWidgets.QMainWindow):
  def __init__(self):
    super(W3Controller,self).__init__()
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
    self.calbutton.clicked.connect(lambda:columncal_button_clicked(self))
    self.closeButton1.clicked.connect(self.closebutton1Clicked)

  def label_fcClicked(self) :
    self.cft='yes' if self.label_fc.isChecked() else 'no'  
    return self.cft

class W4Controller(Ui_CnnctDsgn,W2Controller,QtWidgets.QMainWindow):
  def __init__(self):
    super(W4Controller,self).__init__()
    self.setupUi(self)
    self.setup_control()

  def setup_control(self):
    self.Mg.setText('0')
    self.Vg.setText('0')
    self.sd='yes'
    self.label_selfdesign.clicked.connect(self.selfdesignClicked)
    self.calbutton.clicked.connect(lambda:cnnctdsgn_button_clicked(self))
    self.closeButton1.clicked.connect(self.closebutton1Clicked)

  def selfdesignClicked(self) :
    self.sd='yes' if self.label_selfdesign.isChecked() else 'no'  
    return self.sd