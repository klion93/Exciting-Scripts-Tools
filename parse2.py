#!/usr/bin/python

import parsedos 

trial=parsedos.dos('dos.xml')
with open('S.dat','w') as f:
	f.write('#S_all: E, s, p, d \n')
	for i in range(trial.nw):
		f.write('%g  %g %g %g \n' % (trial.energies[i],trial.speciesl(1,0)[i], trial.speciesl(1,1)[i], trial.speciesl(1,2)[i]))

with open('C.dat','w') as f:
	f.write('#C_all: E, s, p \n')
	for i in range(trial.nw):
		f.write('%g  %g %g \n' % (trial.energies[i],trial.speciesl(2,0)[i], trial.speciesl(2,1)[i]))
		
with open('H.dat','w') as f:
	f.write('#H_all: E, s \n')
	for i in range(trial.nw):
		f.write('%g  %g  \n' % (trial.energies[i],trial.speciesl(3,0)[i]))		


with open('interstitial.dat','w') as f:
        f.write(' e, Inter \n')
        for i in range(trial.nw):
                f.write('%g  %g \n' % (trial.energies[i],trial.interstitial()[i]))

with open('total.dat','w') as f:
	f.write(' e, TDOS \n')
	for i in range(trial.nw):
		f.write('%g  %g \n' % (trial.energies[i],trial.total()[i]))


