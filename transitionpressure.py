import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import rc
import pylab as py 
import math
from scipy.optimize import fsolve, fmin

### Constants #####################################
_e    =  1.602176565e-19         # elementary charge
Bohr  =  5.291772086e-11         # a.u. to meter
Ha2eV = 27.211396132             # Ha to eV
ToGPa = (_e*Ha2eV)/(1e9*Bohr**3) # Ha/[a.u.]^3 to GPa
###################################################


### Functions #####################################
def E_eos(parameters, V):
	""" Birch-Murnaghan Energy"""
	E0, V0, B0, Bp = parameters
	E = E0 + (9.*B0*V0/16)*(((((V0/V)**(2./3))-1.)**3.)*Bp \
		+ ((((V0/V)**(2/3.))-1.)**2.)*(6.-4.*((V0/V)**(2./3.))))
	return E

def geradengleichung_zweipunkte(x1, y1, x2, y2, x):
	"""Einfache Geradengleichung in Zweipunkteform"""
	y = (y2 - y1) / (x2 - x1) * (x-x1) + y1
	return y

def P_eos(parameters, V):
	""" Birch-Murnaghan Pressure"""
	E0, V0, B0, Bp = parameters
	P = 3./2*B0*((V0/V)**(7./3) - 
        (V0/V)**(5./3))*(1. + 3./4*(Bp-4.)*((V0/V)**(2./3) - 1.))
	return P

def V_gesucht(V, P_eos, P0, parameters):
	"""Function for finding specific volume of beta-GaO where P0 is reached."""
	return (P0 / ToGPa) - P_eos(parameters[1],V)

def tangente_para(V, E_eos, P_eos, parameters):
	"""System of nonlinear equations for common tangente calculation"""
	return [ -P_eos(parameters[0],V[0]) + P_eos(parameters[1],V[1]), 
		E_eos(parameters[0],V[0]) + P_eos(parameters[0],V[0]) * V[0] - 
		E_eos(parameters[1],V[1]) - P_eos(parameters[1],V[1]) * V[1] ]

def gather_parameters(data_name):
	"""Gathers BM fit parameters, stores them in list"""
	parameters = np.genfromtxt(data_name, unpack=True, comments="#", skip_header=1)
	return parameters

def gather_BM_data(data_name):
	"""Gathers PDOS data and stores each row in dictionary, returns dic"""
	data = np.genfromtxt(data_name, unpack=True, comments="#", skip_header=1)
	data_dic = {}	
	for spalte in range(len(data)):
		if spalte < 1:
			data_dic["V"] = data[spalte]
		else:
			data_dic["E"] = data[spalte]	
	return data_dic		
##################################################    

## Gathering BM parameters + fit data
para_alpha = gather_parameters('alpha_BM_para.out')
para_beta = gather_parameters('beta_BM_para.out')

BMdata_alpha = gather_BM_data('BM_alpha_fit.out')
BMdata_beta = gather_BM_data('BM_beta_fit.out')
##################################################

###### Calcultion of Transition Pressure using common tangent #######

# Numerical calculation with numpy
parameters = [ para_alpha, para_beta]
transition_volumes = fsolve(tangente_para, [650, 700], xtol=0.000001, 
	args=(E_eos, P_eos, parameters))
transition_energies = []
transition_energies.append(E_eos(parameters[0], transition_volumes[0]))
transition_energies.append(E_eos(parameters[1], transition_volumes[1]))
transition_pressure = P_eos(parameters[0], transition_volumes[0])
pressure_GPa = round(transition_pressure*ToGPa,3)
# Plot data for the tangent
tanx = np.linspace(600,750,100)
tany = geradengleichung_zweipunkte(transition_volumes[0], transition_energies[0],
	 transition_volumes[1], transition_energies[1], tanx)

##################################################

## Plot of Fit Data ##
# Plot properties
fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlabel(r"Volume [Bohr$^3$]", fontsize=17)
plt.ylabel("Energy [Ha]", fontsize=17)
# Set label style
ax.ticklabel_format(useOffset=False, style='sci', axis='both', scilimits=(-2,3))
ax.xaxis.major.formatter._useMathText = True # damit 10^3 etc.
ax.yaxis.major.formatter._useMathText = True # damit 10^3 etc.

# Actual plot
ax.plot(BMdata_alpha["V"], BMdata_alpha["E"],
	 'b', label=r'Birch-Murnaghan fit for $\alpha$ phase')
ax.plot(BMdata_beta["V"], BMdata_beta["E"], 
	'r', label=r'Birch-Murnaghan fit for $\beta$ phase')
ax.plot(tanx, tany, '--',
		color='black', label='Common tangent')
ax.plot(transition_volumes[0], transition_energies[0], 'or',
	transition_volumes[1], transition_energies[1], 'ob')
plt.text(0.1,0.1, r'P$_{\mathrm{transition}}$ = ' 
	+str(round(transition_pressure*ToGPa,3))+' GPa'      
	, transform = ax.transAxes, 
	bbox={'facecolor':'none', 'edgecolor':'black', 'pad':10}, fontsize=15)

plt.legend(prop={'size':10})
plt.savefig('Transitionpressure.pdf', bbox_inches='tight', dpi=1000)


###### Find specific pressure/volume combination ##

# gesucht p = 0.5GPa, p = 2.5 GPa für beta phase
# V_druck_05 = fsolve(V_gesucht, [700], xtol=0.000001, args=(P_eos, 0.5, parameters))
# print(V_druck_05)
# V_druck_25 = fsolve(V_gesucht, [700], xtol=0.000001, args=(P_eos, 2.5, parameters))
# print(V_druck_25)

# V_0 = 715.0484080774
# ratio_volume = V_0 / V_druck_05
# ratio_volume2 = V_0 / V_druck_25
# print(ratio_volume)
# print(ratio_volume2)

# DeltaV / V0 = e_xx + e_yy + e_zz = 3 * e
# volume_change = (V_0 - V_druck_05) / V_0
# volume_change1 = (V_0 - V_druck_25) / V_0
# print(volume_change / 3)
# print(volume_change1 / 3)

# V_druck_exciting_05 = 713.1865016428
# V_druck_exciting_25 = 705.1041835868
# print(P_eos(parameters[1],V_druck_exciting_05)*ToGPa)
# print(P_eos(parameters[1],V_druck_exciting_25)*ToGPa)
