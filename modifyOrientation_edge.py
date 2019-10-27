import math
import numpy as np

def degree2mat(z=0,y=0,x=0):
    (z1,y1,x1)=np.radians((z,y,x))
#    print z1,y1,x1
    return euler2mat(z1,y1,x1)


def euler2mat(z=0, y=0, x=0):
    Ms0 = np.eye(3)
    Ms1 = np.eye(3)
    Ms2 = np.eye(3)
    if z:
        cosz = math.cos(z)
        sinz = math.sin(z)
        Ms0=np.array(
                [[cosz, sinz, 0],
                 [-sinz, cosz, 0],
                 [0, 0, 1]])
    if y:
        cosy = math.cos(y)
        siny = math.sin(y)
        Ms1=np.array(
                [[cosy, 0, -siny],
                 [0, 1, 0],
                 [siny, 0, cosy]])
    if x:
        cosx = math.cos(x)
        sinx = math.sin(x)
        Ms2=np.array(
                [[cosx, sinx, 0],
                 [-sinx, cosx, 0],
                 [0, 0, 1]])
    Ms=np.dot(np.dot(Ms2,Ms1),Ms0)
    if Ms.any():
        return Ms
    return np.eye(3)

# psi theta phi
def mat2euler(M, cy_thresh=None):
    M = np.asarray(M)
    if cy_thresh is None:
        try:
            cy_thresh = np.finfo(M.dtype).eps * 4
        except ValueError:
            cy_thresh = _FLOAT_EPS_4
    r11, r12, r13, r21, r22, r23, r31, r32, r33 = M.flat
    cy = math.sqrt(r33*r33)
    if  cy > cy_thresh: 
        z = math.atan2(r32, r31) 
        y = math.acos(r33) 
        x = math.atan2(r23, -r13) 
    else: 
        z = math.atan2(-r21,  r11)
        y = math.acos(r33) 
        x = 0.0
    return z, y, x

def matZ(gama):
    m=[[np.cos(gama),0,-np.sin(gama)],[0,1,0],[np.sin(gama),0,np.cos(gama)]]
    return np.array(m,dtype=float)
r=matZ(np.arctan(0.5*(5**0.5-1)))
forg=open('run1_ct29_data_expanded.star','r')

i=0

for line in forg:
    i=i+1
    if i < 26:
        print line,
    elif i >= 26:
        l=line.split()
        (rot_0,tilt_0,psi_0) = np.array([l[10],l[11],l[12]],dtype=np.float)
        icos_start=degree2mat(float(psi_0), float(tilt_0), float(rot_0))
        icos1=np.dot(r,icos_start)
        (psi_out,tilt_out,rot_out)=np.degrees(mat2euler(icos1))
        #print (rot_0,tilt_0,psi_0), (rot_out,tilt_out,psi_out)
        l[10]=rot_out
        l[11]=tilt_out
        l[12]=psi_out
        l[13]=float(l[13])*4
        l[14]=float(l[14])*4
        for item in l:
            print item,
        print '\n',
    #if i > 28:
    #    break
