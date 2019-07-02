

import numpy as np



def isSameVertex(l1, l2):
    if abs(float(l1[11]) - float(l2[11])) < 0.1 and abs(float(l1[12]) - float(l2[12])) < 0.1:
        return True
    else:
        return False

def indices(value, lst):
     return [i for i,x in enumerate(lst) if x==value]

def handle(j):

    coordName = j[0].split('@')
    coordName = "1"+coordName[0]+'.star'
    print coordName
    coord = open("../particles_portal/"+coordName,'w')
    coord.write("\
data_\n\
\n\
loop_ \n\
_rlnImageName #1 \n\
_rlnMicrographName #2 \n\
_rlnDefocusU #3 \n\
_rlnDefocusV #4 \n\
_rlnDefocusAngle #5 \n\
_rlnVoltage #6 \n\
_rlnAmplitudeContrast #7 \n\
_rlnSphericalAberration #8 \n\
_rlnGroupName #9 \n\
_rlnGroupNumber #10 \n\
_rlnAngleRot #11 \n\
_rlnAngleTilt #12 \n\
_rlnAnglePsi #13 \n\
_rlnOriginX #14 \n\
_rlnOriginY #15 \n\
_rlnClassNumber #16 \n\
_rlnNormCorrection #17 \n\
_rlnRandomSubset #18 \n\
_rlnLogLikeliContribution #19 \n\
_rlnMaxValueProbDistribution #20 \n\
_rlnNrOfSignificantSamples #21 \n\
_rlnCoordinateX #22\n\
_rlnCoordinateY #23\n")

    k=np.pi/180.0

    (rot,tilt,psi) = np.array([float(j[10])*k,float(j[11])*k,float(j[12])*k],dtype=np.float)
        
    t = np.array([np.cos(psi),-np.sin(psi)],dtype=np.float)*np.sin(tilt)*567+720
    coord.write(j[0]+" "+coordName.split('.')[0]+".mrc ")
    for item in j[2:13]:
        oord.write(item+" ")
    coord.write("0.0 0.0 ")
    for item in j[15:21]:
        coord.write(item+" ")
    coord.write(str(t[0]-float(j[13]))+' '+str(t[1]-float(j[14]))+'\n')
    coord.close()


if __name__=='__main__':
    forg=open('frombin4_run1_expanded.star','r')
    fo = forg.readlines()
    i=0
    o=len(fo)

    for line in fo:
        i=i+1
        if i < 26:
            print line,
        elif i == 26:
            print "_rlnCoordinateX #22"
            print "_rlnCoordinateY #23"
            l=line.split()
            handle(l)
        else:
            l=line.split()
            handle(l)


    #f=open("euler.txt",'r')
    #eular=f.read().split('\n')[:-1]
    #i=1
    #for line in eular:
        #(rot_0,tilt_0,psi_0) = np.array(line.split(),dtype=np.float)
        #icos_start=degree2mat(float(psi_0), float(tilt_0), float(rot_0))
        #print icos_start
        #cos_start=np.linalg.inv(icos_start)
        #print icos_start.T
        #icos1=np.dot(icos_start.T,[0,0,75])
	#print icos1
        #print 90+icos1[0],90+icos1[1],1
        #i=i+1
    #f.close()
