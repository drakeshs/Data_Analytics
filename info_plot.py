#! /usr/bin/env python 

#v1.0.0
#***************************************************************************************************************
#Plots the results obtained from employee info 
#Code should be ran from the directory where the Database has been stored
#****************************************************************************************************************

#importing modules

import csv
import os 
import sys 
import shutil
import numpy as np 
import matplotlib.pyplot as plt

# Riskiness is determned to be directly proportional to the gender score
y1 = 45 #female score
y2 = 55 #male score

#values in the x axis
x = np.arange(1)

#Set width of the bars
width = 0.35

#Plot male and female levels of riskiness
fig, ax = plt.subplots()
barWomen = ax.bar(x, y1, width, color='r')
barMen = ax.bar(x+width, y2, width, color='b')

#add legend
ax.set_ylabel('Riskiness')
ax.set_title('Riskiness According to Gender')
ax.legend( (barMen[0], barWomen[0]), ('Male', 'Female') )

#plot the riskiness according to citizenship
#Costa Rica, Eritrea, Nepal, Peru, Sweden, United States 
N = 6
valueCitizenship = (15, 10, 20, 20, 30, 20)

xCitizen = np.arange(N)
width = 0.5

fig, cx = plt.subplots()
barCitizen = cx.bar(xCitizen, valueCitizenship, width, color='k')

cx.set_ylabel('Riskiness')
cx.set_title('Riskiness According to Citizenship')
cx.set_xticks(xCitizen+width/2)
cx.set_xticklabels(('CR', 'ER', 'NP', 'PE', 'SW', 'US'))

#plot the riskiness according to marital status
#Married, Divorced, Single 
N = 3
valueMarital = (5, 50, 45)

xMarital = np.arange(N)
width = 0.5

fig, mx = plt.subplots()
barMarital = mx.bar(xMarital, valueMarital, width, color='k')

mx.set_ylabel('Riskiness')
mx.set_title('Riskiness According to Marital Status')
mx.set_xticks(xMarital+width/2)
mx.set_xticklabels(('Married', 'Divorced', 'Single'))


#plot the riskiness according to age
#20-30, 30-40, 40-50, 50-60, 60-70, 70-80
N = 6
valueAge = (15, 25, 25, 20, 10, 5)

xAge = np.arange(N)
width = 0.5

fig, agx = plt.subplots()
barAge = agx.bar(xAge, valueAge, width, color='k')

agx.set_ylabel('Riskiness')
agx.set_title('Riskiness According to Age')
agx.set_xticks(xAge+width/2)
agx.set_xticklabels(('less than 20', '30-40', '40-50', '50-60', '60-70', 'greater than 70'))

#show plots
plt.show()
