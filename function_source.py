import math

def get_EandG_vaule():
    ElasticM=2040 #tf/cm2
    ShearM=ElasticM/2/(1+0.25)
    return ElasticM,ShearM

def steel_material_info(keyin):
    #[fy,fu, ?] unit:tf/cm2
    chart={'A36': [2.5,4.2,4.9], 'A572': [3.3,4.9,4.9],'SN490': [3.3,4.9,4.9],'SM570M': [4.2,5.7,5.6]}
    result=chart.get(keyin,'none')
    fy=result[0]
    fu=result[1]
    return fy,fu

def steel_fabrication_info(keyin):
    #鋼材殘餘應力
    chart={'焊接': 1.16, '熱軋': 0.7}
    return chart.get(keyin,'none')

def concrete_material_info(keyin):
    #f'c unit: tf/cm2
    chart={'fc280(4000psi )': 0.28, 'fc350(5000psi)': 0.35, 'fc420(6000psi)': 0.42, 'fc560(8000psi)': 0.56}
    return chart.get(keyin,'none')

def section_property(B,D,tw,tf,sectionshape):
    if sectionshape =='I型': 
        ####################     I型柱    #########################
        Area=B*tf*2+(D-2*tf)*tw
        Ix =(B*(D**3)-(B-tw)*(D-2*tf)**3)/12              #Moment of Inertia cm4
        Iy=((D-2*tf)*tw**3+2*tf*B**3)/12
        Sx=Ix/D*2
        Sy=Iy/B*2
        rx=(Ix/Area)**0.5
        ry=(Iy/Area)**0.5
        JJ=(2*B*tf**3+(D-tf)*tw**3)/3         #Torsion Constant cm4
        Cw=(Iy*(D-tf)**2)/4                         #斷面翹曲常數
        Zx=(B*(D**2)-(B-tw)*(D-2*tf)**2)/4              #Plastic ModuLus
        Zy=((D-2*tf)*tw**2+2*tf*B**2)/4
        Awy=D*tw
        Awx=2*B*tf
    elif sectionshape =='箱型':
        ####################     焊接箱型柱    #########################
        Area=B*D-(B-2*tw)*(D-2*tf)
        Ix =(B*(D**3)-(B-2*tw)*(D-2*tf)**3)/12              #Moment of Inertia cm4
        Iy=(D*(B**3)-(D-2*tf)*(B-2*tw)**3)/12
        Sx=Ix/D*2
        Sy=Iy/B*2
        rx=(Ix/Area)**0.5
        ry=(Iy/Area)**0.5
        JJ=(2*tw*tf*(B-tw)**2*(D-tf)**2)/(B*tw+D*tf-tw**2-tf**2)    #Torsion Constant cm4
        Cw=(B*D)**2/24*(B*tw-D*tf)**2/(B*tw+D*tf)**2*(B*tf-D*tw)                    #斷面翹曲常數
        Zx=(B*(D**2)-(B-2*tw)*(D-2*tf)**2)/4              #Plastic ModuLus
        Zy=(D*(B**2)-(D-2*tf)*(B-2*tw)**2)/4
        Awy=(D-2*tf)*tw*2
        Awx=(B-2*tw)*tf*2
    return Area,Ix,Iy,Sx,Sy,rx,ry,JJ,Cw,Zx,Zy,Awx,Awy

#結實斷面檢核
def section_compact (sectionshape,B,D,tw,tf,fy,Fr,SteelMade,element):
    if sectionshape =='I型': 
        ####################     I型斷面檢核    #########################
        if element=='彎' :   #給梁
            lumdaW=(D-2*tf)/tw
            lumdaF=0.5*B/tf
            lumdaFpd=14/(fy**0.5)
            lumdaFp=17/(fy**0.5)
            if SteelMade.currentText() !='焊接' :
                lumdaFr=37/((fy-Fr)**0.5)
            else :
                lumdaFr=28/((fy-Fr)**0.5)
            lumdaWpd=138/(fy**0.5)
            lumdaWp=170/(fy**0.5)
            lumdaWr=260/((fy-Fr)**0.5)
        else :              #給柱
            lumdaW=(D-2*tf)/tw
            lumdaF=0.5*B/tf
            lumdaFpd=14/(fy**0.5)
            lumdaFp=16/(fy**0.5)
            lumdaFr=25/(fy**0.5)
            lumdaWpd=90/(fy**0.5)   #隨便寫的
            lumdaWp=90/(fy**0.5)    #隨便寫的
            lumdaWr=260/(fy**0.5)
    else :
        ####################     箱型斷面檢核    ######################### 目前給柱而已
        lumdaF=(B-2*tw)/tf
        lumdaW=(D-2*tf)/tw
        lumdaFp=50/(fy**0.5)
        lumdaFr=63/(fy**0.5)
        lumdaWp=lumdaFp
        lumdaWr=lumdaFr
        if SteelMade.currentText() == '焊接':
            lumdaFpd=30/(fy**0.5)
        else :
            lumdaFpd=45/(fy**0.5)
        lumdaWpd=lumdaFpd
    if lumdaF<=lumdaFpd and lumdaW<=lumdaWpd :
        section='塑性設計斷面'
    elif lumdaF<=lumdaFp and lumdaW<=lumdaWp :
        section='結實斷面'
    elif lumdaF<=lumdaFr and lumdaW<=lumdaWr :
        section='半結實斷面'
    else :
        section='細長斷面'
    return section,lumdaW

#梁lRFD強度計算
def Cal_Mn (Lb,Cb,fy,FL,Area,Sx,Sy,Zx,Zy,Iy,ry,Cw,JJ,ElasticM,ShearM,sectionshape):    
    X1=math.pi/Sx*(ElasticM*ShearM*JJ*Area/2)**0.5
    X2=4*Cw/Iy*(Sx/(ShearM*JJ))**2   
    Mpx=fy*Zx/100
    Mrx=FL*Sx/100
    Mny=min(fy*Zy,1.5*fy*Sy)/100 #unit: tf-m
    if sectionshape =='I型': 
        ####################     I型梁    #########################
        Lp=80*ry/(fy**0.5)
        Lr=ry*X1/FL*(1+(1+X2*FL**2)**0.5)**0.5
    elif sectionshape =='箱型':
        ####################     矩型梁    #########################
        Lp=260*ry/(Mpx*100)*(JJ*Area)**0.5
        Lr=4000*ry/(Mrx*100)*(JJ*Area)**0.5

    if Lb<=Lp :
        Mnx_base=Mpx
    elif Lb<=Lr :
        Mnx_base=Mpx-(Mpx-Mrx)*(Lb-Lp)/(Lr-Lp)
    else :
        if sectionshape =='I型': 
            Mnx_base=math.pi/Lb*(ElasticM*Iy*ShearM*JJ+(math.pi*ElasticM/Lb)**2*Iy*Cw)**0.5/100
        else :
            Mnx_base=4000*(JJ*Area)**0.5/Lb*ry/100
            
    Mnx=Cb*Mnx_base
    phiMnx=0.9*min(Mpx,Cb*Mnx_base)
    phiMny=0.9*Mny
    return Lp,Lr,Mpx,Mnx,Mny,phiMnx,phiMny,Mrx

#柱lRFD強度計算
def Cal_Pnc(sectionshape,cft,B,D,tw,tf,Area,fc,fy,ElasticM,Kx,Ky,Lx,Ly,rx,ry):
    if sectionshape =='I型': 
        ####################     I型柱    #########################
        if cft =='yes':
            c1=0.7
            c2=0.6
            c3=0.2
            Ar=0
            # Ec=12000*(fc*1000)**0.5
            Ec=0.83*(10630*(fc*1000)**0.5+70310)/1000 #tf/cm2
            Ac=(B+15)*(D+15)-Area
            Fmy=fy+c1*4.2*(Ar/Area)+c2*fc*(Ac/Area) #tf/cm2
            Em=ElasticM+c3*Ec*Ac/Area #tf/cm2
        else :
            Fmy=fy
            Em=ElasticM 

        lumdac_x=Kx*Lx/rx/math.pi*(Fmy/Em)**0.5
        lumdac_y=Ky*Ly/ry/math.pi*(Fmy/Em)**0.5
        lum=max(lumdac_x, lumdac_y)      
        if lum <= 1.5 :
            Pnc=math.exp(-0.419*lum**2)*Fmy*Area
        else :
            Pnc=0.877/(lum**2)*Fmy*Area
    else :
        ####################     焊接箱型柱    #########################
        if cft =='yes':
            c1=1
            c2=0.85
            c3=0.4
            Ar=0
            # Ec=12000*(fc*1000)**0.5
            Ec=0.83*(10630*(fc*1000)**0.5+70310)/1000 #tf/cm2
            Ac=(B-2*tw)*(D-2*tf)
            Fmy=fy+c1*4.2*(Ar/Area)+c2*fc*(Ac/Area) #tf/cm2
            Em=ElasticM+c3*Ec*Ac/Area #tf/cm2
            # lumdac_x=Kx*Lx/rx/math.pi*(Fmy/Em)**0.5
            # lumdac_y=Ky*Ly/ry/math.pi*(Fmy/Em)**0.5
            # lum=max(lumdac_x, lumdac_y)
        else :
            Fmy=fy
            Em=ElasticM 
        lumdac_x=Kx*Lx/rx/math.pi*(Fmy/Em)**0.5
        lumdac_y=Ky*Ly/ry/math.pi*(Fmy/Em)**0.5
        lum=max(lumdac_x, lumdac_y)
        if lum <= 1.5 :
            Pnc=(0.211*lum**3-0.57*lum**2-0.06*lum+1)*Fmy*Area
        else :
            Pnc=0.764/(lum**2)*Fmy*Area
    phiPnc=0.85*Pnc
    Pnt=fy*Area
    phiPnt=0.9*Pnt
    return Pnc,phiPnc,Pnt,phiPnt,lumdac_x,lumdac_y


#剪力強度計算
def Cal_ShearStrength(lumdaW,fy,Aw,Vu=0):
    kv=5
    if lumdaW<=50*(kv/fy)**0.5 :
        Vn=0.6*fy*Aw
    elif lumdaW<=62*(kv/fy)**0.5 :
        Vn=0.6*fy*Aw*50*(kv/fy)**0.5/lumdaW
    elif lumdaW<=260 :
        Vn=1860*kv/(lumdaW**2)*Aw
    else :
        Vn=0
    phiVny=0.9*Vn
    shearratio=Vu/phiVny
    return Vn,phiVny,shearratio

def Get_Bolt_Diameter(keyin):
    chart={'M19': 1.9, 'M22': 2.2, 'M24': 2.4, 'M27': 2.7, 'M30': 3}
    db=chart.get(keyin,'none')
    dh_bolt=db+0.15
    d_bolt=db+0.3
    return db,dh_bolt,d_bolt

def Get_Bolt_Strength(keyin):
    chart={'F10T-N': [7.5,4], 'F10T-X': [7.5,5], 'A325-N': [6.3,3.36], 'A325-X': [6.3,4.2], 'A490-N': [7.95,4.2], 'A490-N': [7.95,5.25]}
    result=chart.get(keyin,'none')
    Fnt=result[0]
    Fnv=result[1]
    return Fnt,Fnv