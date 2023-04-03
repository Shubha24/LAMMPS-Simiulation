import numpy as np

natoms = 1000

system_size = 20.0

positions = []

for i in range(natoms):
	positions.append(np.random.rand(3)*system_size)
	
with open('random.data','w') as fdata:
	fdata.write('My first LAMMPS pythone practice Data file Code')
	fdata.write('{} atoms\n'.format(natoms))
	fdata.write('{} atoms types\n'.format(1))
	fdata.write('{} {} xlo xhi\n'.format(0.0 ,system_size))
	fdata.write('{} {} ylo yhi\n'.format(0.0 ,system_size))
	fdata.write('{} {} zlo zhi\n'.format(0.0 ,system_size))
	fdata.write('\n')
    fdata.write('Atoms\n\n')

for pos in enumerate(positions):
	fdata.write('{} 1 {} {} {} {}'.format(i+1, *pos))
