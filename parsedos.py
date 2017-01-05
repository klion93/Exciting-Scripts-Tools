#!/usr/bin/python

from lxml import etree
import sys
import numpy as np
from math import *
import os

class dos:
	def __init__(self, name):
		if os.path.isfile(name):
			self.setparameter(name)
		else:
			print "\nScript needs xml file\"",name,"\"to run\n"
			sys.exit()
	def setparameter(self,name):
			self.tree = etree.parse(name)
			self.filename=name
			self.natoms=len(self.tree.xpath('/dos/partialdos'))
			xa = self.tree.xpath('/dos/totaldos/diagram/point/@e')
			self.energies = [float(xe)*27.21138 for xe in xa]
			self.nw=len(self.energies)

	def getdos(self,array):
		pdos=np.zeros(self.nw)
		for m in array:
			mdos = [float(xe) for xe in m.xpath("./point/@dos")]
			for i in range(self.nw):
				pdos[i] = pdos[i] + mdos[i]
		return  pdos

	def total(self):
		xa = self.tree.xpath('/dos/totaldos/diagram/point/@dos')
		tdos = [float(xe) for xe in xa]
		return tdos
	
	def species(self, species):
		m_array =self.tree.xpath('/dos/partialdos[@speciesrn="%s"]/diagram'%(species))
		pdos=self.getdos(m_array)
		return pdos
	
	def atom(self, species, atom):
		m_array =self.tree.xpath('/dos/partialdos[@speciesrn="%s"][@atom="%s"]/diagram'%(species,atom))
		pdos=self.getdos(m_array)
		return pdos

	def angular(self, l):
		m_array =self.tree.xpath('/dos/partialdos/diagram[@l="%s"]'%(l))
		pdos=self.getdos(m_array)
		return pdos
		
	def speciesl(self, species,l):
		m_array =self.tree.xpath('/dos/partialdos[@speciesrn="%s"]/diagram[@l="%s"]'%(species,l))
		pdos=self.getdos(m_array)
		return pdos

	def atoml(self, species,atom,l):
		m_array =self.tree.xpath('/dos/partialdos[@speciesrn="%s"][@atom="%s"]/diagram[@l="%s"]'%(species,atom,l))
		pdos=self.getdos(m_array)
		return pdos

	def atomlm(self, species,atom,l,m):
		m_array =self.tree.xpath('/dos/partialdos[@speciesrn="%s"][@atom="%s"]/diagram[@l="%s"][@m="%s"]'%(species,atom,l,m))
		pdos=self.getdos(m_array)
		return pdos

	def interstitial(self):
		m_array =self.tree.xpath('/dos/interstitialdos/diagram')
		pdos=self.getdos(m_array)
		return pdos
