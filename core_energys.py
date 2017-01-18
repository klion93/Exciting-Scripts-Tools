import numpy as np 

def ha_to_ev(value_in_ha):
	"""Converting unit in Ha to eV, returns eV value"""
	umrechnungs_faktor = 27.2113825435
	value_in_eV = value_in_ha * umrechnungs_faktor
	return value_in_eV

C1_Ha = -9.609639899	
C21_Ha = -9.572980922
C22_Ha = -9.574630727
C3_Ha = -9.594418696 

C1_eV = ha_to_ev(C1_Ha)
C21_eV = ha_to_ev(C21_Ha)
C22_eV = ha_to_ev(C22_Ha)
C3_eV = ha_to_ev(C3_Ha)

print(C1_eV)
print(C21_eV)
print(C22_eV)
print(C3_eV)