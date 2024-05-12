#!/usr/bin/env python
# coding: utf-8

# In[1]:


from vpython import *
dict={'intensity':[],'time':[]}
#plot the graph
g1 = graph(title="Solar Intensity",xtitle="time (min)",ytitle="Local Intensity [J/m^2]",width=500, height=250)
f1 = gcurve(color=color.blue)
R=1#radius
#creat
earth=sphere(pos=vector(0,0,0),radius=R, texture=textures.earth,shininess=0)
choose=int(input('1:winter solstice, 2:spring equinox or autumnal equinox, 3:summer solstice'))
if choose==1:#winter solstice
    #tilt represent where direct solar radiation
    tilt = -23.5*pi/180
    #rotate the earth
    earth.rotate(origin=vector(0,0,0),axis=vector(0,0,1),angle=tilt)
    #set the rotation axis negative x positive y
    Npole = cylinder(pos=vector(0,0,0),axis=1.5*R*vector(-sin(tilt),cos(tilt),0),radius=0.02*R)
    Spole = cylinder(pos=vector(0,0,0),axis=-1.5*R*vector(-sin(tilt),cos(tilt),0),radius=0.02*R)     
    #set the latitude
    lat = 23*pi/180
    ball = sphere(pos=R*vector(-cos(lat),sin(lat),0),radius=0.01,color=color.yellow, make_trail=False)
    #set the point on Kaohsiung
    ball.rotate(angle=-149.5*pi/180,origin=vector(0,0,0),axis=vector(0,1,0))
    ball.rotate(angle=-23.3*pi/180,origin=vector(0,0,0),axis=vec(0,0,1))
    #draw trail
    ball.make_trail=True  
    #angular velocity of earth rotation
    w = 0.004374*norm(Npole.axis)
    t = 0 #initial time
    dt = 0.1#interval time
    Is = 1360*vector(1,0,0)#intensity of light
    while t<1436.48396:#one day
        rate(1000)#how many calculation per second
      #rotate the earth
        earth.rotate(axis=w, angle=mag(w)*dt)#every time how far its go(w*dt)
      #rotate the dot
        ball.v = cross(w,ball.pos)
        ball.pos = ball.pos + ball.v*dt
      #inverse the direction
        I = -dot(Is,ball.pos)
        dict['intensity'].append(I)
        if I<0:
            f1.plot(t,0)#night
        else:
            f1.plot(t,I)#morning
        dict['time'].append(t)
        t = t + dt#refresh the time
if choose==2:#spring equinox or autumnal equinox
    tilt = 0*pi/180#tilt represent where direct solar radiation
    #rotate the earth
    earth.rotate(origin=vector(0,0,0),axis=vector(0,0,1),angle=tilt)
    #set the rotation axis negative x positive y
    Npole = cylinder(pos=vector(0,0,0),axis=1.5*R*vector(-sin(tilt),cos(tilt),0),radius=0.02*R) 
    Spole = cylinder(pos=vector(0,0,0),axis=-1.5*R*vector(-sin(tilt),cos(tilt),0),radius=0.02*R)    
    #set the latitude
    lat = 23*pi/180
    ball = sphere(pos=R*vector(-cos(lat),sin(lat),0),radius=0.01,color=color.yellow, make_trail=False)
    #set the point on Kaohsiung
    ball.rotate(angle=-149.5*pi/180,origin=vector(0,0,0),axis=vector(0,1,0))
    ball.rotate(angle=0*pi/180,origin=vector(0,0,0),axis=vec(0,0,1))
    #draw trail
    ball.make_trail=True   
    #angular velocity of earth rotation
    w = 0.004374*norm(Npole.axis)
    t = 0 #initial time
    dt = 0.1#interval time
    Is = 1360*vector(1,0,0)#intensity of light    
    while t<1436.48396:#one day
        rate(1000)#how many calculation per second
        #rotate the earth
        earth.rotate(axis=w, angle=mag(w)*dt)#every time how far its go(w*dt)
        #rotate the dot
        ball.v = cross(w,ball.pos)
        ball.pos = ball.pos + ball.v*dt
        #inverse the direction
        I = -dot(Is,ball.pos)
        dict['intensity'].append(I)
        if I<0:
            f1.plot(t,0)#night
        else:
            f1.plot(t,I)#morning
        dict['time'].append(t)
        t = t + dt#refresh the time
if choose==3:#summer solstice
    tilt = 23.5*pi/180#tilt represent where direct solar radiation
    #rotate the earth
    earth.rotate(origin=vector(0,0,0),axis=vector(0,0,1),angle=tilt)
    #set the rotation axis negative x positive y
    Npole = cylinder(pos=vector(0,0,0),axis=1.5*R*vector(-sin(tilt),cos(tilt),0),radius=0.02*R)
    Spole = cylinder(pos=vector(0,0,0),axis=-1.5*R*vector(-sin(tilt),cos(tilt),0),radius=0.02*R)  
    #set the latitude
    lat = 23*pi/180
    ball = sphere(pos=R*vector(-cos(lat),sin(lat),0),radius=0.01,color=color.yellow, make_trail=False)
    #set the point on Kaohsiung
    ball.rotate(angle=-149.5*pi/180,origin=vector(0,0,0),axis=vector(0,1,0))
    ball.rotate(angle=23.3*pi/180,origin=vector(0,0,0),axis=vec(0,0,1))
    #draw trail
    ball.make_trail=True   
    #angular velocity of earth rotation
    w = 0.004374*norm(Npole.axis)
    t = 0 #initial time
    dt = 0.1#interval time
    Is = 1360*vector(1,0,0)#intensity of light
    while t<1436.48396:#one day
        rate(1000)#how many calculation per second
        #rotate the earth
        earth.rotate(axis=w, angle=mag(w)*dt)#every time how far its go(w*dt)
        #rotate the dot
        ball.v = cross(w,ball.pos)
        ball.pos = ball.pos + ball.v*dt
        #inverse the direction
        I = -dot(Is,ball.pos)
        dict['intensity'].append(I)
        if I<0:
            f1.plot(t,0)#night
        else:
            f1.plot(t,I)#morning
        dict['time'].append(t)
        t = t + dt#refresh the time


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[3]:


Intensity=list(map(float,dict['intensity']))
time=list(map(float,dict['time']))


# In[4]:


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.Series(Intensity)


# In[5]:


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.Series(time)


# In[6]:


len(Intensity)


# In[7]:


I_sum=0
for i in range(0,14364):
    if Intensity[i]>0:
        I_sum=I_sum+Intensity[i]
    else:
        I_sum=I_sum
print(I_sum)

