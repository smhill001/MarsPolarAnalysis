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
temp=0

OppositionDates=["2005-11-07","2007-12-24","2010-01-29","2012-03-03",
                 "2014-04-08","2016-05-22","2018-07-27"]
LineColorList=np.array([[0.4,0.2,0.6],[0.1,0.1,0.7],[0.1,0.6,0.1],
                        [0.6,0.5,0.2],[0.6,0.1,0.0],[0.0,0.0,0.0],
                        [0.5,0.5,0.5]])

axN,axS=MPL.SetupMarsPlot()

MarsObs=MPL.MarsMeasData(fn)
for od in OppositionDates:
    MarsObs.load_select_data("Test","Test",od)
    
    for CaporHood in ["Cap","Hood"]:
    
        Indices = [k for k, x in enumerate(MarsObs.PoleandObject) if x[1:4] == "NP"+CaporHood[0]] #what does this do!?
        Latitude=[MarsObs.Latitude[index] for index in Indices]
        hlon=[MarsObs.hlon[index] for index in Indices]
        Ls_array=np.array(hlon)-(35.4377+49.5581)
        Ls_array=np.mod(Ls_array+180.0,360.)-180.
        if CaporHood=="Cap":
            mkr='o'
            axN.scatter(np.array(Ls_array,dtype=float),np.array(Latitude,dtype=float),
                       marker=mkr,s=15,color=LineColorList[np.mod(temp,7)],alpha=1.0,linewidths=0,label=od)       
        elif CaporHood=="Hood":
            mkr='+'
            axN.scatter(np.array(Ls_array,dtype=float),np.array(Latitude,dtype=float),
                       marker=mkr,s=15,color=LineColorList[np.mod(temp,7)],alpha=1.0,linewidths=0)
        
        Indices = [k for k, x in enumerate(MarsObs.PoleandObject) if x[1:4] == "SP"+CaporHood[0]] #what does this do!?
        Latitude=[MarsObs.Latitude[index] for index in Indices]
        hlon=[MarsObs.hlon[index] for index in Indices]
        Ls_array=np.array(hlon)-(35.4377+49.5581)
        Ls_array=np.mod(Ls_array+180.0,360.)-180.
        if CaporHood=="Cap":
            mkr='o'
        elif CaporHood=="Hood":
            mkr='+'
        axS.scatter(np.array(Ls_array,dtype=float),np.array(Latitude,dtype=float),
                   marker=mkr,s=15,color=LineColorList[np.mod(temp,7)],alpha=1.0,linewidths=0,label=od)
    temp=temp+1
    axN.legend(loc=2,ncol=3,fontsize=6,scatterpoints=1)
    #axS.legend(loc=2,ncol=3,fontsize=6,scatterpoints=1)
###############################################################################
#Solar Latitude as a function of season

pl.savefig("f:\\Astronomy\Projects\Planets\Mars\Imaging Data\Mapping\Mars_Seasons.png",dpi=300)

###############################################################################
#Mars Seasonal Coverage by Terrestrial Year
canvas=pl.figure(figsize=(4.5, 4.5), dpi=150,facecolor="white")
canvas.add_subplot(1,1,1,axisbg="white") 

MarsObs.load_all_data()
All_Ls_array=np.array(MarsObs.hlon)-(35.4377+49.5581)
All_Ls_array=np.mod(All_Ls_array+180.0,360.)-180.
date=[]
for i in range(0,len(MarsObs.DateTimeString)):
    date.append(np.datetime64(MarsObs.DateTimeString[i]))

x0,x1,xtks=-180.,180.,13
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