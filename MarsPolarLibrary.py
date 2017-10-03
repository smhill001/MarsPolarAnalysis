# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 07:42:34 2016

@author: Astronomy
"""

class MarsMeasData:
    def __init__(self,filename):
        import ephem
        import numpy as np
       
        #        
        self.DateTimeString=[]
        self.PoleandObject=[]
        self.Latitude=[]
        self.hlon=[]
        self.hlat=[]
        self.NRecords=0

        MarsMeasData_DataFile=open(filename,'r')
        MarsMeasData_Lines=MarsMeasData_DataFile.readlines()
        MarsMeasData_DataFile.close()
        nrecords=len(MarsMeasData_Lines)
        self.NRecords=nrecords

        for i in range(1,nrecords):
            fields=MarsMeasData_Lines[i].split(',')
            #print fields

            tempdate=fields[4][1:11]
            temptime1=fields[5][1:6]
            temptime2=fields[5][7:8]
            if int(temptime2) <=1:
                datetimestring= tempdate+" "+temptime1+":0"+str(6*int(temptime2))#+"UT"
            elif int(temptime2) >1:
                datetimestring= tempdate+" "+temptime1+":"+str(6*int(temptime2))#+"UT"
            datetimestring=datetimestring.replace("/", "-")

            self.DateTimeString.append(datetimestring)
            self.PoleandObject.append(fields[1])
            self.Latitude.append(float(fields[10]))
            
            Planet = ephem.Mars(datetimestring)
            hltemp=float(Planet.hlon)*180./np.pi
            self.hlon.append(hltemp)
            hltemp=float(Planet.hlat)*180./np.pi
            self.hlat.append(hltemp)