import numpy as np
import math
from function_source import *

def beamcal_button_clicked(data):
    try:
        fy, fu =steel_material_info(data.SteelStrength.currentText())
        Fr=steel_fabrication_info(data.SteelMade.currentText())
        B=float(data.width.text())
        D=float(data.depth.text())
        tw=float(data.tw.text())
        tf=float(data.tf.text())
        Lb=float(data.unbracedL.text())
        Cb=float(data.Cb.text())
        Mux=float(data.Mux.text())
        Vuy=float(data.Vuy.text())
        ElasticM,ShearM=get_EandG_vaule()
        FL=fy-Fr

        #斷面資訊
        [Area,Ix,Iy,Sx,Sy,rx,ry,JJ,Cw,Zx,Zy,Awx,Awy]=section_property(B,D,tw,tf,'I型')

        #結實斷面檢核
        [section,lumdaW]=section_compact('I型',B,D,tw,tf,fy,Fr,data.SteelMade,'彎')

        #梁lRFD強度計算
        [Lp,Lr,Mpx,Mnx,Mny,phiMnx,phiMny,Mrx]=cal_Mn(Lb,Cb,fy,FL,Area,Sx,Sy,Zx,Zy,Iy,ry,Cw,JJ,ElasticM,ShearM,'I型')  
        pmmratio=Mux/phiMnx
            
        #剪力強度計算
        [Vny,phiVny,shearratio]=cal_ShearStrength(lumdaW,fy,Awy,Vuy)

        #結果輸出
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
        #梁結果
        result1='Mpx= '+str(round(Mpx,2))+'  tf-m'
        result2='Mnx= '+str(round(phiMnx/0.9,2))+'  tf-m'
        result3='Mny= '+str(round(Mny,2))+'  tf-m'
        result4='\u03d5 Mnx= '+str(round(phiMnx,2))+'  tf-m'
        result5='\u03d5 Mny= '+str(round(phiMny,2))+'  tf-m'
        result6='Vny= '+str(round(Vny,2))+'  tf'
        result7='\u03d5 Vny= '+str(round(phiVny,2))+'  tf'
        result8='PMM Ratio= '+str(round(pmmratio,3))
        result9='Shear Ratio= '+str(round(shearratio,3))

        data.textBrowser.setText((section+'\n'+info1+'\n'+info2+'\n'+info3+'\n'+info4+'\n'+info5+'\n'+info6+'\n'+
                                    info7+'\n'+info8+'\n'+info9+'\n'+info10+'\n'+info11+'\n'+info12+'\n'
                                    +result1+'\n'+result2+'\n'+result3+'\n'+result4+'\n'+result5+'\n'+result6+'\n'+result7+'\n'+result8+'\n'+result9 ))
        
                
        #畫圖
        x=[0,Lp,Lr]
        y=[0.9*Mpx,0.9*Mpx,0.9*Mrx]
        z0=np.linspace(Lr,2*Lr,5)
        z1=[]

        for i in z0 :
            z1.append(0.9*draw_CalMn(i,Mpx,Mrx,Lp,Lr,ElasticM,Iy,ShearM,Cw,JJ))
            x.append(i)
        for i in z1 :
            y.append(i)
            
        xCb=[0,Lp]
        yCb=[0.9*Mpx,0.9*Mpx]
        z2=np.linspace(Lp,2*Lr,20)
        z3=[]
        for i in z2 :
            z3.append(0.9*min(Mpx,Cb*draw_CalMn(i,Mpx,Mrx,Lp,Lr,ElasticM,Iy,ShearM,Cw,JJ)))
            xCb.append(i)
        for i in z3 :
            yCb.append(i)
            
        data.mplwidget.canvas.axes.clear()
        data.mplwidget.canvas.axes.plot(xCb,yCb, linestyle='--',color='orange')
        data.mplwidget.canvas.axes.plot(x,y)
        data.mplwidget.canvas.axes.plot(Lb,Mux,marker='o', markersize=3,color='red')
        data.mplwidget.canvas.axes.set_xlabel('Lb(cm)', fontsize=8, color='white')
        data.mplwidget.canvas.axes.set_ylabel('\u03c6 Mn(tf-m)', fontsize=8, color='white')
        data.mplwidget.canvas.axes.grid(True,linestyle='--', color='black')
        data.mplwidget.canvas.draw()
    except :
        data.textBrowser.setText('Please input the parameters')
       

        
def draw_CalMn(Lb,Mpx,Mrx,Lp,Lr,ElasticM,Iy,ShearM,Cw,JJ) :
    if Lb<=Lp :
        Mnx=Mpx
    elif Lb<=Lr :
        Mnx=Mpx-(Mpx-Mrx)*(Lb-Lp)/(Lr-Lp)
    else :
        Mnx=math.pi/Lb*(ElasticM*Iy*ShearM*JJ+(math.pi*ElasticM/Lb)**2*Iy*Cw)**0.5/100
    return Mnx
