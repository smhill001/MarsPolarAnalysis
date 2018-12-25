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
        import ephem
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
            self.DateTime.append(np.datetime64(datetimestring))
            self.PoleandObject.append(fields[1])
            self.Latitude.append(float(fields[10]))
            
            Planet = ephem.Mars(datetimestring)
            hltemp=float(Planet.hlon)*180./np.pi
            self.hlon.append(hltemp)
            hltemp=float(Planet.hlat)*180./np.pi
            self.hlat.append(hltemp)

    def load_select_data(self,Pole,Type,OppositionDate):
        import ephem
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
                self.DateTime.append(np.datetime64(datetimestring))
                self.PoleandObject.append(fields[1])
                self.Latitude.append(float(fields[10]))
            
                Planet = ephem.Mars(datetimestring)
                hltemp=float(Planet.hlon)*180./np.pi
                self.hlon.append(hltemp)
                hltemp=float(Planet.hlat)*180./np.pi
                self.hlat.append(hltemp)
            
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

    canvas.add_subplot(3,1,2,axisbg="white") 
    y0,y1,ytks=-30.,30.,13
    pl.xlim(x0,x1)
    # Set x ticks
    pl.xticks(np.linspace(x0,x1,xtks, endpoint=True))
    # Set y limits
    pl.ylim(y0,y1)
    # Set y ticks
    pl.yticks(np.linspace(y0,y1,ytks, endpoint=True))
    pl.grid(linewidth=0.5)
    pl.tick_params(axis='y', which='major', labelsize=9)
    pl.tick_params(labelbottom=False)
    pl.ylabel("Solar Latitude (deg)",fontsize=9)
    
    pl.title(Target,fontsize=9)
    
    LS_array=np.linspace(-180.,180.,73.)
    SolLat=25.*np.sin(LS_array*np.pi/180.)
    
    pl.plot(LS_array,SolLat,color='k',label="Solar Latitude (deg)")
    
    Seasons=['Autumn','Winter','Spring','Summer']
    for j in range(0,len(Seasons)):
        pl.annotate(Seasons[j],xy=(-135.+90.*j,27.5),size=9,horizontalalignment='center',verticalalignment='center')
        pl.annotate(Seasons[np.mod(j+2,4)],xy=(-135.+90.*j,-27.5),size=9,horizontalalignment='center',verticalalignment='center')
        
    pl.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.09)

    return axN,axS


   