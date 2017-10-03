# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 13:03:32 2016

@author: Astronomy
"""

import sys
sys.path.append('f:\\Astronomy\Python Play')
sys.path.append('f:\\Astronomy\Python Play\marstime-0.4.6')
sys.path.append('f:\\Astronomy\Python Play\Mars')
#import marstime
#import ephem
import numpy as np
import matplotlib.pyplot as pl
import MarsPolarLibrary as MPL
import datetime

fn="f:\\Astronomy\Projects\Planets\Mars\Imaging Data\Mapping\HillMars_mea.CSV"

MarsObs=MPL.MarsMeasData(fn)
    

x0=-180.
x1=180.
xtks=13

y0=30
y1=90
ytks=13

Target="North Pole"

canvas=pl.figure(figsize=(6.5, 4.5), dpi=150,facecolor="white")
canvas.add_subplot(3,1,1,axisbg="white") 


Ls_array=np.array(MarsObs.hlon)-(35.4377+49.5581)

pl.xlim(x0,x1)
# Set x ticks
pl.xticks(np.linspace(x0,x1,xtks, endpoint=True))
# Set y limits
pl.ylim(y0,y1)
# Set y ticks
pl.yticks(np.linspace(y0,y1,ytks, endpoint=True))
#pl.yscale('log')
pl.grid()
pl.tick_params(axis='both', which='major', labelsize=6)
pl.ylabel("Latitude (deg)",fontsize=7)
#pl.xlabel("Solar Longitude, Ls (deg)",fontsize=7)
pl.title(Target,fontsize=9)

NPHIndices = [k for k, x in enumerate(MarsObs.PoleandObject) if x[1:4] == "NPH"] #what does this do!?
NPHLatitude=[MarsObs.Latitude[index] for index in NPHIndices]
NPHhlon=[MarsObs.hlon[index] for index in NPHIndices]
NPHLs_array=np.array(NPHhlon)-(35.4377+49.5581)
NPHLs_array=np.mod(NPHLs_array+180.0,360.)-180.
pl.scatter(np.array(NPHLs_array,dtype=float),np.array(NPHLatitude,dtype=float),
           marker='o',s=10,color='b',alpha=1.0,linewidths=0,label='Hood')

NPCIndices = [k for k, x in enumerate(MarsObs.PoleandObject) if x[1:4] == "NPC"] #what does this do!?
NPCLatitude=[MarsObs.Latitude[index] for index in NPCIndices]
NPChlon=[MarsObs.hlon[index] for index in NPCIndices]
NPCLs_array=np.array(NPChlon)-(35.4377+49.5581)
NPCLs_array=np.mod(NPCLs_array+180.0,360.)-180.
pl.scatter(np.array(NPCLs_array,dtype=float),np.array(NPCLatitude,dtype=float),
           marker='o',s=10,color='k',alpha=1.0,linewidths=0,label='Cap')

LS_ALPO=np.linspace(40,135,20)
LAT_ALPO=[65.1,67.4,67.6,68.0,69.7,72.2,74.0,75.5,77.8,79.8,
          81.2,81.6,82.7,83.1,82.9,82.4,82.8,83.5,83.6,83.4]
pl.plot(LS_ALPO,LAT_ALPO,color='k',label="ALPO 1980-2003 Average")


pl.legend(loc=4,ncol=1,fontsize=6,scatterpoints=1)



Target="South Pole"

y0=-90
y1=-30
ytks=13
canvas.add_subplot(3,1,3,axisbg="white") 
pl.xlim(x0,x1)
# Set x ticks
pl.xticks(np.linspace(x0,x1,xtks, endpoint=True))
# Set y limits
pl.ylim(y0,y1)
# Set y ticks
pl.yticks(np.linspace(y0,y1,ytks, endpoint=True))
#pl.yscale('log')
pl.grid()
pl.tick_params(axis='both', which='major', labelsize=6)
pl.ylabel("Latitude (deg)",fontsize=7)
pl.xlabel("Solar Longitude, Ls (deg)",fontsize=7)
pl.title(Target,fontsize=9)

SPHIndices = [k for k, x in enumerate(MarsObs.PoleandObject) if x[1:4] == "SPH"] #what does this do!?
SPHLatitude=[MarsObs.Latitude[index] for index in SPHIndices]
SPHhlon=[MarsObs.hlon[index] for index in SPHIndices]
SPHLs_array=np.array(SPHhlon)-(35.4377+49.5581)
SPHLs_array=np.mod(SPHLs_array+180.0,360.)-180.
pl.scatter(np.array(SPHLs_array,dtype=float),np.array(SPHLatitude,dtype=float),
           marker='o',s=10,color='b',alpha=1.0,linewidths=0,label='Hood')

SPCIndices = [k for k, x in enumerate(MarsObs.PoleandObject) if x[1:4] == "SPC"] #what does this do!?
SPCLatitude=[MarsObs.Latitude[index] for index in SPCIndices]
SPChlon=[MarsObs.hlon[index] for index in SPCIndices]
SPCLs_array=np.array(SPChlon)-(35.4377+49.5581)
SPCLs_array=np.mod(SPCLs_array+180.0,360.)-180.
pl.scatter(np.array(SPCLs_array,dtype=float),np.array(SPCLatitude,dtype=float),
           marker='o',s=10,color='k',alpha=1.0,linewidths=0,label='Cap')

LS_ALPO=np.linspace(200,300,21)-360.
W_ALPO=[54.0,51.2,49.1,47.4,44.4,40.4,38.2,35.1,31.3,28.9,23.9,
        21.6,20.6,19.2,16.8,16.0,14.6,12.1,9.8,9.5,10.6]
LAT_ALPO=-(90.-np.array(W_ALPO)/2.)
pl.plot(LS_ALPO,LAT_ALPO,color='k',label="ALPO 1986-2003 Average")

pl.legend(loc=4,ncol=1,fontsize=6,scatterpoints=1)

Target="Solar Latitude"

y0=-30
y1=30
ytks=13
canvas.add_subplot(3,1,2,axisbg="white") 
pl.xlim(x0,x1)
# Set x ticks
pl.xticks(np.linspace(x0,x1,xtks, endpoint=True))
# Set y limits
pl.ylim(y0,y1)
# Set y ticks
pl.yticks(np.linspace(y0,y1,ytks, endpoint=True))
#pl.yscale('log')
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


canvas=pl.figure(figsize=(4.5, 4.5), dpi=150,facecolor="white")
canvas.add_subplot(1,1,1,axisbg="white") 
Ls_array=np.array(MarsObs.hlon)-(35.4377+49.5581)
print Ls_array
Ls_array=np.mod(Ls_array+180.0,360.)-180.
print Ls_array
#print MarsObs.DateTimeString
date=[]
for i in range(0,len(MarsObs.DateTimeString)):
    date.append(np.datetime64(MarsObs.DateTimeString[i]))
#date_list_datetime.append(np.datetime64(datetimestring))

x0=-180.
x1=180.
xtks=13



#LS Coverage as a function of year

#Ls_array=np.array(MarsObs.hlon)-(35.4377+49.5581)

pl.xlim(x0,x1)
# Set x ticks
pl.xticks(np.linspace(x0,x1,xtks, endpoint=True))
# Set y limits
#pl.ylim(y0,y1)
# Set y ticks
#pl.yticks(np.linspace(y0,y1,ytks, endpoint=True))
#pl.yscale('log')
pl.grid()
pl.tick_params(axis='both', which='major', labelsize=6)
pl.ylabel("Year",fontsize=7)
pl.xlabel("Solar Longitude, Ls (deg)",fontsize=7)
pl.title("LS Coverage",fontsize=9)

pl.scatter(Ls_array,date,marker='o',s=10,color='k',alpha=1.0,linewidths=0)

pl.savefig("f:\\Astronomy\Projects\Planets\Mars\Imaging Data\Mapping\Mars_Coverage.png",dpi=300)

