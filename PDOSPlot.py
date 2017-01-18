import numpy as np 
import matplotlib.pyplot as plt

def gather_pdos_data(data_name):
	"""Gathers PDOS data and stores each row in dictionary, returns dic"""
	data = np.genfromtxt(data_name, unpack=True, comments="#", skip_header=1)
	data_dic = {}
	orbital = ["s", "p", "d", "f"]
	for spalte in range(len(data)):
		if spalte < 1:
			data_dic["E"] = data[spalte]
		else:
			data_dic[orbital[spalte-1]] = data[spalte]
	return data_dic			

plt.close("all")


# Gathering all data for PDOS
C_all_data_dic = gather_pdos_data("C.dat")
total_dos = gather_pdos_data("total.dat")
S_all_data_dic = gather_pdos_data("S.dat")
H_all_data_dic = gather_pdos_data("H.dat")
C1_dic  = gather_pdos_data("C1_LR.dat")
C21_dic = gather_pdos_data("C2_LOR_RUL.dat")
C22_dic = gather_pdos_data("C2_LOL_RUR.dat")
C3_dic  = gather_pdos_data("C3_LR.dat")

# Plot properties
fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlim(0,max(total_dos["E"]))
plt.ylim(0,120)
plt.xlabel("Energy [eV]", fontsize=17)
plt.ylabel("DOS [states/eV]", fontsize=17)

# Plotting specific data
#ax.plot(C_all_data_dic["E"], C_all_data_dic["s"], 'r', label='PDOS C(s)')
ax.plot(C_all_data_dic["E"], C_all_data_dic["p"], c='blue', label='PDOS C(p)')
ax.plot(C1_dic["E"], C1_dic["p"], c='red', label='PDOS C1(p)')
ax.plot(C21_dic["E"], C21_dic["p"], c='green', label='PDOS C21(p)')
ax.plot(C22_dic["E"], C22_dic["p"], c='cyan', label='PDOS C22(p)')
ax.plot(C3_dic["E"], C3_dic["p"], c='black', label='PDOS C3(p)')


# ax.plot(S_all_data_dic["E"], S_all_data_dic["s"], 'b', label='PDOS S(s)')
# ax.plot(S_all_data_dic["E"], S_all_data_dic["p"], c='cyan', label='PDOS S(p)')
# ax.plot(H_all_data_dic["E"], H_all_data_dic["s"], 'g', label='PDOS H(s)')
# ax.plot(total_dos["E"], total_dos["s"], c='0.9', label='Total DOS')
#ax.fill_between(total_dos["E"], total_dos["s"],  0, color='0.9')
plt.legend(prop={'size':10})
# plt.setp(ax.lines)

# Saving file
plt.savefig('PDOS_C_contributions.png', bbox_inches='tight', dpi=350)
plt.close(1)