import matplotlib.pyplot as plt
import numpy as np 


#### Functions ######

def gather_spectra_data(data_name):
	"""Gather Spectra data and store rows in dictionary, return dic"""
	data = np.genfromtxt(data_name, unpack=True, comments="#",usecols=(0,2))
	data_dic = {}
	for spalte in range(len(data)):
		data_dic[spalte] = data[spalte]
	return data_dic

#####################

# Gathering Spectra data
C1_epsilon_11 = gather_spectra_data(
	data_name = "../Mol1/C_1_links/EPSILON_BSEsinglet_SCRfull_OC11.OUT")
C1_epsilon_22 = gather_spectra_data(
	data_name = "../Mol1/C_1_links/EPSILON_BSEsinglet_SCRfull_OC22.OUT")
C1_epsilon_33 = gather_spectra_data(
	data_name = "../Mol1/C_1_links/EPSILON_BSEsinglet_SCRfull_OC33.OUT")
C1_epsilon_13 = gather_spectra_data(
	data_name = "../Mol1/C_1_links/EPSILON_BSEsinglet_SCRfull_OC13.OUT")

# Plotting properties
fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlim(255,280)
# plt.ylim(0,120)      
plt.xlabel("Energy [eV]", fontsize=17)
plt.ylabel(r"Im $\epsilon_{\mathrm{M}}$ [arb. unit]", fontsize=17)



# Tick properties
ax.ticklabel_format(useOffset=False, style='sci', axis='both', scilimits=(-2,3))
ax.xaxis.major.formatter._useMathText = True # damit 10^3 etc.
ax.yaxis.major.formatter._useMathText = True # damit 10^3 etc.

# Actual Plot
ax.plot(C1_epsilon_11[0], C1_epsilon_11[1], c='black', label=r'C1 xx')
ax.plot(C1_epsilon_22[0], C1_epsilon_22[1], c='blue', label=r'C1 yy')
ax.plot(C1_epsilon_33[0], C1_epsilon_33[1], c='red', label=r'C1 zz')
ax.plot(C1_epsilon_13[0], C1_epsilon_13[1], c='green', label=r'C1 xz')


plt.legend(prop={'size':15})

# Saving file
plt.savefig('C1_spectra.pdf', bbox_inches='tight', dpi=1000)