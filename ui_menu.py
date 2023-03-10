# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu(object):
    def setupUi(self, menu):
        menu.setObjectName("menu")
        menu.resize(431, 319)
        menu.setStyleSheet("background-color:rgba(16, 30, 41, 240);")
        self.centralwidget = QtWidgets.QWidget(menu)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 40, 160, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title1 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.title1.setFont(font)
        self.title1.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"font: 25 9pt \"Bookman Old Style\";\n"
"color: rgb(255,255,255)")
        self.title1.setFrame(False)
        self.title1.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.title1.setObjectName("title1")
        self.verticalLayout_2.addWidget(self.title1)
        self.FlexCal = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.FlexCal.setStyleSheet("QPushButton#FlexCal{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"\n"
"}\n"
"\n"
"QPushButton#FlexCal:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}\n"
"\n"
"QPushButton#FlexCal:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/beam_1.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.FlexCal.setIcon(icon)
        self.FlexCal.setObjectName("FlexCal")
        self.verticalLayout_2.addWidget(self.FlexCal)
        self.ColumnCal = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ColumnCal.setStyleSheet("QPushButton#ColumnCal{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"\n"
"}\n"
"\n"
"QPushButton#ColumnCal:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}\n"
"\n"
"QPushButton#ColumnCal:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/buildings.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.ColumnCal.setIcon(icon1)
        self.ColumnCal.setObjectName("ColumnCal")
        self.verticalLayout_2.addWidget(self.ColumnCal)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(220, 40, 160, 91))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.title2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.title2.setFont(font)
        self.title2.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"font: 25 9pt \"Bookman Old Style\";\n"
"color: rgb(255,255,255)")
        self.title2.setFrame(False)
        self.title2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.title2.setObjectName("title2")
        self.verticalLayout_3.addWidget(self.title2)
        self.CnnctDsgn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.CnnctDsgn.setStyleSheet("QPushButton#CnnctDsgn{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"\n"
"}\n"
"\n"
"QPushButton#CnnctDsgn:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}\n"
"\n"
"QPushButton#CnnctDsgn:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}")
        self.CnnctDsgn.setIcon(icon)
        self.CnnctDsgn.setObjectName("CnnctDsgn")
        self.verticalLayout_3.addWidget(self.CnnctDsgn)
        self.background2 = QtWidgets.QLabel(self.centralwidget)
        self.background2.setGeometry(QtCore.QRect(20, 20, 391, 281))
        self.background2.setStyleSheet("background-color:rgba(0,0,0,200);\n"
"border-radius:20px;")
        self.background2.setText("")
        self.background2.setObjectName("background2")
        self.background2.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)

    def retranslateUi(self, menu):
        _translate = QtCore.QCoreApplication.translate
        menu.setWindowTitle(_translate("menu", "MainWindow"))
        self.title1.setText(_translate("menu", "           Calculation"))
        self.FlexCal.setText(_translate("menu", "  I-Shaped Beam"))
        self.ColumnCal.setText(_translate("menu", " Column"))
        self.title2.setText(_translate("menu", "              Design"))
        self.CnnctDsgn.setText(_translate("menu", " Connection"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menu = QtWidgets.QMainWindow()
    ui = Ui_Menu()
    ui.setupUi(menu)
    menu.show()
    sys.exit(app.exec_())
