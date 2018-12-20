# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 13:03:32 2016

@author: Astronomy
"""

import sys
sys.path.append('f:\\Astronomy\Python Play')
sys.path.append('f:\\Astronomy\Python Play\marstime-0.4.6')
sys.path.append('f:\\Astronomy\Python Play\Mars')
import numpy as np
import matplotlib.pyplot as pl
import MarsPolarLibrary as MPL

###############################################################################
#Mars Polar Observations as a function of season
fn="f:/Astronomy/Projects/Planets/Mars/Imaging Data/Mapping/HillMars_mea.CSV"

MarsObs=MPL.MarsMeasData(fn)
MarsObs.load_all_data()
All_Ls_array=np.array(MarsObs.hlon)-(35.4377+49.5581)
    
canvas=pl.figure(figsize=(6.5, 4.5), dpi=150,facecolor="white")
x0,x1,xtks=-180.,180.,13
temp=0

for Pole in ["North","South"]:
    Target=Pole+" Pole"
    canvas.add_subplot(3,1,1+temp,axisbg="white") 
    temp=temp+2   
    y0,y1,ytks=25.,90.,14
    
    pl.xlim(x0,x1)
    pl.xticks(np.linspace(x0,x1,xtks, endpoint=True))
    
    if Pole=="North":
        pl.ylim(y0,y1)
        pl.yticks(np.linspace(y0,y1,ytks, endpoint=True))
    elif Pole=="South":
        pl.ylim(-y1,-y0)
        pl.yticks(np.linspace(-y1,-y0,ytks, endpoint=True))
        
    pl.grid()
    pl.tick_params(axis='both', which='major', labelsize=6)
    pl.ylabel("Latitude (deg)",fontsize=7)
    pl.title(Target,fontsize=9)

    for CaporHood in ["Cap","Hood"]:
    
        Indices = [k for k, x in enumerate(MarsObs.PoleandObject) if x[1:4] == Pole[0]+"P"+CaporHood[0]] #what does this do!?
        #THIS IS WHERE TO INSERT A LOOP FOR APPARITION FOR COLOR CYCLING
        Latitude=[MarsObs.Latitude[index] for index in Indices]
        hlon=[MarsObs.hlon[index] for index in Indices]
        Ls_array=np.array(hlon)-(35.4377+49.5581)
        Ls_array=np.mod(Ls_array+180.0,360.)-180.
        if CaporHood=="Cap":
            clr='k'
        elif CaporHood=="Hood":
            clr='b'
        pl.scatter(np.array(Ls_array,dtype=float),np.array(Latitude,dtype=float),
                   marker='o',s=10,color=clr,alpha=1.0,linewidths=0,label=CaporHood)
    
    if Pole=="North":
        LS_ALPO=np.linspace(40,135,20)
        LAT_ALPO=[65.1,67.4,67.6,68.0,69.7,72.2,74.0,75.5,77.8,79.8,
                  81.2,81.6,82.7,83.1,82.9,82.4,82.8,83.5,83.6,83.4]
        LAT_SD_ALPO=[4.4,4.5,3.4,2.4,2.4,2.1,1.4,1.8,2.8,2.9,
                     2.5,2.2,1.3,1.5,1.6,1.8,1.9,1.0,0.7,0.6]
        pl.plot(LS_ALPO,LAT_ALPO,color='k',label="ALPO 1980-2003 Average")
        pl.plot(LS_ALPO,np.array(LAT_ALPO)+1.96*np.array(LAT_SD_ALPO),color='k',linewidth=0.5,label="95% Confidence")
        pl.plot(LS_ALPO,np.array(LAT_ALPO)-1.96*np.array(LAT_SD_ALPO),color='k',linewidth=0.5)
    elif Pole=="South":
        LS_ALPO=np.linspace(200,300,21)-360.
        W_ALPO=[54.0,51.2,49.1,47.4,44.4,40.4,38.2,35.1,31.3,28.9,23.9,
                21.6,20.6,19.2,16.8,16.0,14.6,12.1,9.8,9.5,10.6]
        LAT_SD_ALPO=[7.1,6.5,4.6,5.5,4.9,7.5,7.8,6.5,6.1,5.4,4.2,
                     3.1,1.7,2.2,2.2,2.3,3.0,3.2,1.8,1.4,1.0]
        LAT_ALPO=-(90.-np.array(W_ALPO)/2.)
        pl.plot(LS_ALPO,LAT_ALPO,color='k',label="ALPO 1986-2003 Average")
        pl.plot(LS_ALPO,np.array(LAT_ALPO)+1.96*np.array(LAT_SD_ALPO),color='k',linewidth=0.5,label="95% Confidence")
        pl.plot(LS_ALPO,np.array(LAT_ALPO)-1.96*np.array(LAT_SD_ALPO),color='k',linewidth=0.5)
        
    pl.legend(loc=4,ncol=1,fontsize=6,scatterpoints=1)
###############################################################################
#Solar Latitude as a function of season
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
pl.grid()
pl.tick_params(axis='both', which='major', labelsize=6)
pl.ylabel("Solar Latitude (deg)",fontsize=7)

pl.title(Target,fontsize=9)

LS_array=np.linspace(-180.,180.,73.)
SolLat=25.*np.sin(LS_array*np.pi/180.)

pl.plot(LS_array,SolLat,color='k',label="Solar Latitude (deg)")

Seasons=['Autumn','Winter','Spring','Summer']
for j in range(0,len(Seasons)):
    pl.annotate(Seasons[j],xy=(-135.+90.*j,27.5),size=7,horizontalalignment='center',verticalalignment='center')
    pl.annotate(Seasons[np.mod(j+2,4)],xy=(-135.+90.*j,-27.5),size=7,horizontalalignment='center',verticalalignment='center')
    
pl.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.09)

pl.savefig("f:\\Astronomy\Projects\Planets\Mars\Imaging Data\Mapping\Mars_Seasons.png",dpi=300)

###############################################################################
#Mars Seasonal Coverage by Terrestrial Year
canvas=pl.figure(figsize=(4.5, 4.5), dpi=150,facecolor="white")
canvas.add_subplot(1,1,1,axisbg="white") 
All_Ls_array=np.mod(All_Ls_array+180.0,360.)-180.
date=[]
for i in range(0,len(MarsObs.DateTimeString)):
    date.append(np.datetime64(MarsObs.DateTimeString[i]))

pl.xlim(x0,x1)
pl.xticks(np.linspace(x0,x1,xtks, endpoint=True))
pl.grid()
pl.tick_params(axis='both', which='major', labelsize=6)
pl.ylabel("Year",fontsize=7)
pl.xlabel("Solar Longitude, Ls (deg)",fontsize=7)
pl.title("LS Coverage",fontsize=9)

pl.scatter(All_Ls_array,date,marker='o',s=10,color='k',alpha=1.0,linewidths=0)
DateIndices = [k for k, x in enumerate(date) if x > np.datetime64("2018-01-01")] #what does this do!?
for i in DateIndices:
    print date[i]

print date>np.datetime64("2018-01-01")
pl.savefig("f:\\Astronomy\Projects\Planets\Mars\Imaging Data\Mapping\Mars_Coverage.png",dpi=300)