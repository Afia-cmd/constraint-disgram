## this program should take user inputs and graph aircraft constraint diagrams of the ff
##constant level turn
##rate of climb
##cruise airspeed
##stall speed

##the design parameters to be provided are
##minimum drag coeffecient, Cd_min
##bank angle, phi
##aspect ratio, AR
##vertical speed, V
##cruise speed, V
##density at operation altitude, rho
##maximum lift coefficient, Cl_max
##operation altitude, h


import matplotlib.pyplot as plt 
import numpy as np 
import math

##Cd_min = float(input('what is you estimated min drag coefficient? '))
##phi = float(input('what is your bank angle? '))
##AR = float(input('what is the aspect ratio? '))
##Vv = float(input('what is the vertical speed? '))
##V = float(input('what is the cruise speed? '))
##Vs = float(input('what is the stall speed? '))
##rho = float(input('what is the density at the operation altitude? '))
##Cl_max = float(input('what is the max lift coeffecient? '))

Cd_min = 0.01
phi = 30
AR = 8
Vv =3
V_cruise = 20
V_turn = 20
Vy = 15 ## this is the airspeed during climb
Vs = 12


rho = 1.18
Cl_max = 1.8 ##

q_cruise = 0.5*rho*(V_cruise**2)
q_turn = 0.5*rho*(V_turn**2)
q_climb = 0.5*rho*(Vy**2)

n = 1/(np.cos(np.deg2rad(phi)))
print("n = ", n)
#e = 1.78*(1-(0.045*(AR**0.68)))-(0.64)  
e=0.8   #...based on data
print("e = ", e)
k = 1/(math.pi * AR * e)
print("k = ",k)

## get values for the wing loading in N/m^2, the horizontal axis
WS = np.arange(30, 300, 1)

TW_const_lvl_turn = q_turn *( (Cd_min/WS) + k*((n/q_turn)*(n/q_turn))*(WS))
plt.plot(WS, TW_const_lvl_turn, 'r')

TW_cruise_AIRspeed = ((q_cruise)*(Cd_min)*(1/WS))+(k*(1/q_cruise)*(WS))
plt.plot(WS, TW_cruise_AIRspeed, 'b')

TW_RoC = (Vv/Vy) + ((q_climb/WS)*Cd_min)  + ((k/q_climb)*WS)
plt.plot(WS,TW_RoC, 'y')
#print (TW_RoC)

WS_stall = 0.5*rho*(Vs**2)*Cl_max  #wing loading based
plt.axvline(x=WS_stall)
plt.show()
