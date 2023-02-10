import numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore
from ColumnCal import Ui_ColumnCal
import math
from function_source import *

def ColCalButtonClicked(data):    
    try :
        sectionshape=data.section.currentText()
        fy, fu =steel_material_info(data.SteelStrength.currentText())
        Fr=steel_fabrication_info(data.SteelMade.currentText())
        fc=concrete_material_info(data.fc.currentText())
        B=float(data.width.text())
        D=float(data.depth.text())
        tw=float(data.tw.text())
        tf=float(data.tf.text())
        Lb=float(data.Ly.text())
        Cb=float(data.Cb.text())
        Lx=float(data.Lx.text())
        Ly=float(data.Ly.text())
        Kx=float(data.Kx.text())
        Ky=float(data.Ky.text())
        Pu=float(data.Pu.text())
        Mux=float(data.Mux.text())
        Muy=float(data.Muy.text())
        Vux=float(data.Vux.text())
        Vuy=float(data.Vuy.text())
        ElasticM,ShearM=get_EandG_vaule()
        FL=fy-Fr

        #斷面資訊
        [Area,Ix,Iy,Sx,Sy,rx,ry,JJ,Cw,Zx,Zy,Awx,Awy]=section_property(B,D,tw,tf,sectionshape)
    
        #柱lRFD強度計算
        [Pnc,phiPnc,Pnt,phiPnt,lumdac_x,lumdac_y]=Cal_Pnc(sectionshape,data.cft,B,D,tw,tf,Area,fc,fy,ElasticM,Kx,Ky,Lx,Ly,rx,ry)

        #結實斷面檢核
        [section,lumdaW]=section_compact(sectionshape,B,D,tw,tf,fy,Fr,data.SteelMade,'壓彎')

        #梁lRFD強度計算
        [Lp,Lr,Mpx,Mnx,Mny,phiMnx,phiMny,Mrx]=Cal_Mn(Lb,Cb,fy,FL,Area,Sx,Sy,Zx,Zy,Iy,ry,Cw,JJ,ElasticM,ShearM,sectionshape)  

        #stress ratio
        if Pu < 0.2*phiPnc :
            pmmratio=Pu/(2*phiPnc)+Mux/phiMnx+Muy/phiMny
        else :
            pmmratio=Pu/phiPnc+8/9*(Mux/phiMnx+Muy/phiMny)

        #剪力強度計算
        [Vny,phiVny,shearratio]=Cal_ShearStrength(lumdaW,fy,Awy,Vuy)


        #結果輸出
        #斷面資訊
        info1='fy= '+str(round(fy,2))+'  tf/cm^2'
        info2='fu= '+str(round(fu,2))+'  tf/cm^2'
        info3='Ix= '+str(round(Ix,2))+'  cm^4'
        info4='Iy= '+str(round(Iy,2))+'  cm^4'
        info5='Sx= '+str(round(Sx,2))+'  cm^3'
        info6='Sy= '+str(round(Sy,2))+'  cm^3'
        info7='Zx= '+str(round(Zx,2))+'  cm^3'
        info8='Zy= '+str(round(Zy,2))+'  cm^3'
        info9='rx= '+str(round(rx,2))+'  cm'
        info10='ry= '+str(round(ry,2))+'  cm'
        info11='Lp= '+str(round(Lp,2))+'  cm'
        info12='Lr= '+str(round(Lr,2))+'  cm'
        info13='\u03bb x= '+str(round(lumdac_x,2))
        info14='\u03bb y= '+str(round(lumdac_y,2))
        info15='Mpx= '+str(round(Mpx,2))+'  tf-m'
        #柱結果
        result1='Pnc= '+str(round(Pnc,2))+'  tf \n'+'Pnt= '+str(round(Pnt,2))+'  tf'
        result2='\u03d5 Pnc= '+str(round(phiPnc,2))+'  tf\n'+'\u03d5Pnt= '+str(round(phiPnt,2))+'  tf'
        #梁結果
        result3='Mnx= '+str(round(Mnx,2))+'  tf-m'
        result4='Mny= '+str(round(Mny,2))+'  tf-m'
        result5='\u03d5 Mnx= '+str(round(phiMnx,2))+'  tf-m'
        result6='\u03d5 Mny= '+str(round(phiMny,2))+'  tf-m'
        result7='Vny= '+str(round(Vny,2))+'  tf'
        result8='\u03d5 Vny= '+str(round(phiVny,2))+'  tf'
        result9='PMM Ratio= '+str(round(pmmratio,3))
        result10='Shear Ratio= '+str(round(shearratio,3))


        data.textBrowser.setText((section+'\n'+info1+'\n'+info2+'\n'+info3+'\n'+info4+'\n'+info5+'\n'+info6+'\n'+
                                info7+'\n'+info8+'\n'+info9+'\n'+info10+'\n'+info11+'\n'+info12+'\n'+info13+'\n'+info14+'\n'+info15+'\n'+
                                result1+'\n'+result2+'\n'+result3+'\n'+result4+'\n'+result5+'\n'+result6+'\n'+result7+'\n'+result8+'\n'+result9+'\n'+result10 ))
        
        # data.textBrowser.setText((info1+'\n'+info2+'\n'+info3+'\n'+info4+'\n'+info5+'\n'+info6+'\n'+info7+'\n'+info8))
            
        #畫圖
        if Pu < 0.2*phiPnc :
            Y=Pu/(2*phiPnc)
            X=Mux/phiMnx+Muy/phiMny
        else :
            Y=Pu/phiPnc
            X=8/9*(Mux/phiMnx+Muy/phiMny)

        data.colmplwidget.canvas.axes.clear()
        data.colmplwidget.canvas.axes.plot([0,0.9,1],[1,0.2,0])
        data.colmplwidget.canvas.axes.plot(X,Y,marker='o', markersize=3,color='red')
        data.colmplwidget.canvas.axes.set_xlabel('Mu(tf-m)', fontsize=8, color='white')
        data.colmplwidget.canvas.axes.set_ylabel('Pu(tf)', fontsize=8, color='white')
        data.colmplwidget.canvas.axes.grid(True,linestyle='--', color='black')
        data.colmplwidget.canvas.draw()
    except :
        data.textBrowser.setText('Please input the parameters')









