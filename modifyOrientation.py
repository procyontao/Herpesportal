
import numpy as np
forg=open('particle_vertices.star','r')

i=0

for line in forg:
    i=i+1
    if i < 28:
        print line,
    elif i >= 28:
        l=line.split()
        l[2]=float(l[2])-550*np.cos(float(l[11])/180.0*np.pi)
        l[3]=float(l[3])-550*np.cos(float(l[11])/180.0*np.pi)
        for item in l:
            print item,
        print '\n',
    #if i > 28:
    #    break
