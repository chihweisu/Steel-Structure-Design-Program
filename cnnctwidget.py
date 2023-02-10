from PyQt5 import QtGui,QtWidgets,QtCore
from PyQt5.QtCore import QThread, Qt, QRect
from PyQt5.QtGui import QPainter, QPen, QColor


class cnnctwidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.drawornot = 'no'
    
    def cnnctdraw_info(self,data,BoltNum_line,d_bolt,CnnctType):
        factor=3*80/float(data.depth.text())
        self.factor=factor
        self.D=float(data.depth.text())*factor
        self.tf=float(data.tf.text())*factor
        self.hplate=float(data.hplate.text())*factor
        self.Bplate=float(data.Bplate.text())*factor
        self.BoltLe=float(data.BoltLe.text())*factor
        self.BoltS=float(data.BoltS.text())*factor
        self.BoltNum_line=BoltNum_line
        self.d_bolt=d_bolt*factor
        self.CnnctType=CnnctType
        if self.CnnctType == 'Pinned' :
            self.clearspan=2*factor
        else :
            self.clearspan=4*factor
        self.drawornot='yes'
        self.update()

    def paintEvent(self, event):
        self.qpainter = QPainter()
        self.qpainter.begin(self)
        palette = self.palette()
        palette.setColor(self.backgroundRole(),QColor(57,66,83))
        self.setAutoFillBackground(True)
        self.setPalette(palette)
        qpen = QPen(Qt.black, 2, Qt.SolidLine)
        self.qpainter.setPen(qpen)


        if self.drawornot =='yes' :

            #Draw 梁
            self.qpainter.setBrush(QColor(112,128,144))
            self.qpainter.drawRect(QRect(10, 5, 250, self.tf))
            self.qpainter.drawRect(QRect(10, 5+self.tf, 240, self.D-2*self.tf))
            self.qpainter.drawRect(QRect(10, 5+self.D-self.tf, 250, self.tf))
            #Draw 柱面
            self.qpainter.drawLine(5, 0, 5, 250)
            #Draw 接合板
            self.qpainter.setPen(Qt.black)
            self.qpainter.setBrush(QColor(105,105,105))
            self.qpainter.drawRect(QRect(5, 125-self.hplate/2,self.Bplate, self.hplate))
            self.qpainter.setPen(Qt.black)
            self.qpainter.setBrush(Qt.white)

            #Draw 螺孔
            for i in range(len(self.BoltNum_line)) :
                first_y=125-self.hplate/2+self.BoltLe-self.d_bolt/2
                x=2*self.factor+self.BoltLe-self.d_bolt/2+i*self.BoltS
                for j in range(self.BoltNum_line[i]) :
                    self.qpainter.drawEllipse(x,first_y+j*self.BoltS,self.d_bolt,self.d_bolt)


        self.qpainter.end()
        


            

        
