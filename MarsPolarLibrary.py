# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 07:42:34 2016

@author: Astronomy
"""


import sys
drive='f:'
sys.path.append(drive+'\\Astronomy\Python Play\Util')

import ConfigFiles as CF

class MarsMeasData(CF.readtextfilelines):
    pass
    def load_all_data(self):
        #import ephem
        import marstime
        from astropy.time import Time
        import numpy as np
        import MarsPolarLibrary as MPL
       
        self.DateTimeString=[]
        self.DateTime=[]
        self.PoleandObject=[]
        self.Latitude=[]
        self.hlon=[]
        self.hlat=[]

        for recordindex in range(1,self.nrecords):
            fields=self.CfgLines[recordindex].split(',')
            datetimestring=MPL.MakeDateTime(fields[4],fields[5])
            self.DateTimeString.append(datetimestring)
            dt64=np.datetime64(datetimestring)
            self.DateTime.append(dt64)
            self.PoleandObject.append(fields[1])
            self.Latitude.append(float(fields[10]))
            #print dt64
            t=Time(str(dt64),format='isot',scale='utc')
            ott=t.jd-2451545.0
            Ls=marstime.Mars_Ls(j2000_ott=ott)
            self.hlon.append(Ls)
            self.hlat.append(marstime.solar_declination(ls=Ls))
            #Planet = ephem.Mars(datetimestring)
            #MAY WANT ADDITIONAL MARS EPHEMERIS PARAMETERS HERE

    def load_select_data(self,Pole,Type,OppositionDate):
        #import ephem
        import marstime
        from astropy.time import Time
        import numpy as np
        import MarsPolarLibrary as MPL
       
        self.DateTimeString=[]
        self.DateTime=[]
        self.PoleandObject=[]
        self.Latitude=[]
        self.hlon=[]
        self.hlat=[]

        Odate64=np.datetime64(OppositionDate)
        for recordindex in range(1,self.nrecords):
            fields=self.CfgLines[recordindex].split(',')
            datetimestring=MPL.MakeDateTime(fields[4],fields[5])
            dt64=np.datetime64(datetimestring)
            if Odate64-180<=dt64<=Odate64+180:
                self.DateTimeString.append(datetimestring)
                self.DateTime.append(dt64)
                self.PoleandObject.append(fields[1])
                self.Latitude.append(float(fields[10]))
            
                t=Time(str(dt64),format='isot',scale='utc')
                ott=t.jd-2451545.0
                Ls=marstime.Mars_Ls(j2000_ott=ott)
                self.hlon.append(Ls)
                self.hlat.append(marstime.solar_declination(ls=Ls))
                #Planet = ephem.Mars(datetimestring)
                #MAY WANT ADDITIONAL MARS EPHEMERIS PARAMETERS HERE
            
def MakeDateTime(datefield,timefield):
    tempdate=datefield[1:11]
    temptime1=timefield[1:6]
    temptime2=timefield[7:8]
    #print temptime2
    if int(temptime2) <=1:
        datetimestring= tempdate+" "+temptime1+":0"+str(6*int(temptime2))#+"UT"
    elif int(temptime2) >1:
        datetimestring= tempdate+" "+temptime1+":"+str(6*int(temptime2))#+"UT"
    datetimestring=datetimestring.replace("/", "-")
    return datetimestring

def SetupMarsPlot():
    import matplotlib.pyplot as pl
    import numpy as np
    import marstime
    from astropy.time import Time
    from astropy import constants as const
 
    canvas=pl.figure(figsize=(8.0, 6.0), dpi=150,facecolor="white")
    x0,x1,xtks=-180.,180.,13
    y0,y1,ytks=25.,90.,14

    #NORTH
    axN=canvas.add_subplot(3,1,1,axisbg="white") 
    
    axN.set_xlim(x0,x1)
    axN.set_xticks(np.linspace(x0,x1,xtks, endpoint=True))
    
    axN.set_ylim(y0,y1)
    axN.set_yticks(np.linspace(y0,y1,ytks, endpoint=True))
        
    axN.grid(linewidth=0.5)
    axN.tick_params(axis='y', which='major', labelsize=9)
    axN.tick_params(labelbottom=False)
    axN.set_ylabel("Latitude (deg)",fontsize=9)
    axN.set_title("North Pole",fontsize=10)
    
    LS_ALPO=np.linspace(40,135,20)
    LAT_ALPO=[65.1,67.4,67.6,68.0,69.7,72.2,74.0,75.5,77.8,79.8,
              81.2,81.6,82.7,83.1,82.9,82.4,82.8,83.5,83.6,83.4]
    LAT_SD_ALPO=[4.4,4.5,3.4,2.4,2.4,2.1,1.4,1.8,2.8,2.9,
                 2.5,2.2,1.3,1.5,1.6,1.8,1.9,1.0,0.7,0.6]
    axN.plot(LS_ALPO,LAT_ALPO,color='k',label="ALPO 1980-2003 Average")
    axN.plot(LS_ALPO,np.array(LAT_ALPO)+1.96*np.array(LAT_SD_ALPO),color='k',linewidth=0.5,label="95% Confidence")
    axN.plot(LS_ALPO,np.array(LAT_ALPO)-1.96*np.array(LAT_SD_ALPO),color='k',linewidth=0.5)
    
    #SOUTH
    axS=canvas.add_subplot(3,1,3,axisbg="white") 
    y0,y1,ytks=25.,90.,14
    
    axS.set_xlim(x0,x1)
    axS.set_xticks(np.linspace(x0,x1,xtks, endpoint=True))
    axS.set_ylim(-y1,-y0)
    axS.set_yticks(np.linspace(-y1,-y0,ytks, endpoint=True))
       
    axS.grid(linewidth=0.5)
    axS.tick_params(axis='both', which='major', labelsize=8)
    axS.set_ylabel("Latitude (deg)",fontsize=9)
    axS.set_xlabel("Solar Longitude (deg)",fontsize=9)
    axS.set_title("South Pole",fontsize=10)
    
    LS_ALPO=np.linspace(200,300,21)-360.
    W_ALPO=[54.0,51.2,49.1,47.4,44.4,40.4,38.2,35.1,31.3,28.9,23.9,
            21.6,20.6,19.2,16.8,16.0,14.6,12.1,9.8,9.5,10.6]
    LAT_SD_ALPO=[7.1,6.5,4.6,5.5,4.9,7.5,7.8,6.5,6.1,5.4,4.2,
                 3.1,1.7,2.2,2.2,2.3,3.0,3.2,1.8,1.4,1.0]
    LAT_ALPO=-(90.-np.array(W_ALPO)/2.)
    axS.plot(LS_ALPO,LAT_ALPO,color='k',label="ALPO 1986-2003 Average")
    axS.plot(LS_ALPO,np.array(LAT_ALPO)+1.96*np.array(LAT_SD_ALPO),color='k',linewidth=0.5,label="95% Confidence")
    axS.plot(LS_ALPO,np.array(LAT_ALPO)-1.96*np.array(LAT_SD_ALPO),color='k',linewidth=0.5)
    
    #SOLAR LATITUDE
    Target="Solar Latitude"

    axL=canvas.add_subplot(3,1,2,axisbg="white") 
    y0,y1,ytks=-30.,30.,13
    axL.set_xlim(x0,x1)
    axL.set_xticks(np.linspace(x0,x1,xtks, endpoint=True))
    axL.set_ylim(y0,y1)
    axL.set_yticks(np.linspace(y0,y1,ytks, endpoint=True))
    axL.grid(linewidth=0.5)
    axL.tick_params(axis='y', which='major', labelsize=9)
    axL.tick_params(labelbottom=False)
    axL.set_ylabel("Solar Latitude (deg)",fontsize=9)
    
    axL.set_title(Target,fontsize=9)
    
    #306 days to start at Autumn equinox rather than vernal equinox
    dateoffset=np.arange(0,686,2,dtype=int)-306 
    datearray=np.datetime64('2000-06-03')+dateoffset
    
    LS_array=[]
    SL_array=[]
    D_array=[]
    F_array=[]
    for d in datearray:
        t=Time(str(d),format='isot',scale='utc')
        ott=t.jd-2451545.0
        LS_temp=marstime.Mars_Ls(j2000_ott=ott)
        SL_temp=marstime.solar_declination(ls=LS_temp)
        D_temp=marstime.heliocentric_distance(j2000_ott=ott)
        F_temp=const.L_sun/(4.*np.pi*(const.au*D_temp)**2)
        print ott,LS_temp,SL_temp,F_temp
        LS_array.append(float(LS_temp))
        SL_array.append(float(SL_temp))
        D_array.append(float(D_temp))
        F_array.append(float(F_temp.value))
    LS_array=np.array(LS_array)
    SL_array=np.array(SL_array)
    
    LS_array=np.mod(LS_array+180.0,360.)-180.
        
    axL.plot(LS_array,SL_array,color='k',label="Solar Latitude (deg)")
    
    axD=axL.twinx()
    axD.set_xlim(x0,x1)
    axD.set_xticks(np.linspace(x0,x1,xtks, endpoint=True))
    axD.set_ylim(500,700)
    axD.set_yticks(np.linspace(400,800,9, endpoint=True))
    axD.tick_params(axis='y', which='major', labelsize=9)
    axD.set_ylabel("Solar Flux (W/m^2)",fontsize=9)

    axD.plot(LS_array,F_array,color='b',label="Solar Distance")
    
    Seasons=['Autumn','Winter','Spring','Summer']
    for j in range(0,len(Seasons)):
        axL.annotate(Seasons[j],xy=(-135.+90.*j,27.5),size=9,horizontalalignment='center',verticalalignment='center')
        axL.annotate(Seasons[np.mod(j+2,4)],xy=(-135.+90.*j,-27.5),size=9,horizontalalignment='center',verticalalignment='center')
   
    pl.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.09)

    return axN,axS


   