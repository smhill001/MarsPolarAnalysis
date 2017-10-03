# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 13:03:32 2016

@author: Astronomy
"""

import sys
sys.path.append('f:\\Astronomy\Python Play')
sys.path.append('f:\\Astronomy\Python Play\marstime-0.4.6')
import marstime
import ephem
import numpy as np
import matplotlib.pyplot as pl
import datetime

print marstime.Mars_Ls(j2000_ott=0.1)
print marstime.j2000_epoch()

observer = ephem.Observer()
observer.lon = ephem.degrees('-104.907985')
observer.lat = ephem.degrees('39.708200')
Planet = ephem.Mars('2016-07-26 03:30:00Z')
Planet.compute(observer)

print Planet.name
print Planet.sun_distance
print Planet.earth_distance
print Planet.size
print Planet.mag
print Planet.phase
#print Planet.radius #Crashes at work
Planet.elong
#print Planet.elong #Crashes at work
#print ephem.degrees(Planet.elong) #Crashes at work
print float(Planet.elong)
print float(Planet.hlon)*180./np.pi
print float(Planet.hlat)*180./np.pi


#fn="f:\\Astronomy\Projects\Planets\Mars\Imaging Data\Mapping\HillMars_mea.CSV"
fn="f:\\Astronomy\Projects\Planets\Mars\Imaging Data\Mapping\Mars_NPC_wse.CSV"
data=np.loadtxt(fn,dtype=str,delimiter=',')

print float(data[1,6])
jd=np.array(data[1:,6],dtype=float)
lat=np.array(data[1:,10],dtype=float)
date=np.zeros(len(data)/19-1)
nrows=len(data)

date_list_string=[]
hlon_array=[]

print "nrows=",nrows
for i in range(0,nrows-1):
    tempdate=data[i+1,4][1:11]
    temptime1=data[i+1,5][1:6]
    temptime2=data[i+1,5][7:8]
    if int(temptime2) <=1:
        datetimestring= tempdate+" "+temptime1+":0"+str(6*int(temptime2))#+"UT"
    elif int(temptime2) >1:
        datetimestring= tempdate+" "+temptime1+":"+str(6*int(temptime2))#+"UT"
    datetimestring=datetimestring.replace("/", "-")
    #date=np.datetime64(datetimestring)
    #date_list_datetime.append(np.datetime64(datetimestring))
    date_list_string.append(datetimestring)
    Planet = ephem.Mars(datetimestring)
    hltemp=float(Planet.hlon)*180./np.pi
    hlon_array.append(hltemp)
    print datetimestring,hltemp
    

x0=-180.
x1=180.
xtks=13

y0=30
y1=90
ytks=13

Target="North Pole"

canvas=pl.figure(figsize=(6.5, 4.5), dpi=150,facecolor="white")
canvas.add_subplot(2,1,1,axisbg="white") 
#pl.figure(figsize=(6.5, 4.5), dpi=150,facecolor="white")
        # Create a new subplot from a grid of 1x1
#ax=fig.add_subplot(1, 1, 1,axisbg="white")


Ls_array=np.array(hlon_array)-(35.4377+49.5581)

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


pl.scatter(Ls_array,lat)

Target="South Pole"

y0=-90
y1=-30
ytks=13
canvas.add_subplot(2,1,2,axisbg="white") 
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


pl.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.09)

pl.savefig("f:\\Astronomy\Projects\Planets\Mars\Imaging Data\Mapping\Mars_NPC_wse.png",dpi=300)
