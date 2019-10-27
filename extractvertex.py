

import numpy as np

rot_index=11-1
tlt_index=12-1
psi_index=13-1
orgX_index=14-1
orgY_index=15-1
img_index=4-1
mic_index=5-1
dU_index=6-1
dV_index=7-1

def isSameVertex(l1, l2):
    if abs(float(l1[tlt_index]) - float(l2[tlt_index])) < 0.1 and abs(float(l1[psi_index]) - float(l2[psi_index])) < 0.1:
        return True
    else:
        return False

def indices(value, lst):
     return [i for i,x in enumerate(lst) if x==value]

def handleGroup(imageGroup):
    groups = [[0]]
    for i in range(1,len(imageGroup)):
        sign = 0
        for g in groups:
            if isSameVertex(imageGroup[i], imageGroup[g[0]]):
                g.append(i)
                sign = 1
        if sign == 0:
            groups.append([i])
    coordName = imageGroup[0][img_index].split('@')
    coordName = "1"+coordName[0]+'.star'
    print coordName
    coord = open("../particles_bin1_normed/"+coordName,'w')

    coord.write("\
data_images\n\
\n\
loop_\n\
_rlnVoltage #1\n\
_rlnAmplitudeContrast #2\n\
_rlnSphericalAberration #3\n\
_rlnImageName #4\n\
_rlnMicrographName #5\n\
_rlnDefocusU #6\n\
_rlnDefocusV #7\n\
_rlnDefocusAngle #8\n\
_rlnGroupName #9\n\
_rlnGroupNumber #10\n\
_rlnAngleRot #11\n\
_rlnAngleTilt #12\n\
_rlnAnglePsi #13\n\
_rlnOriginX #14\n\
_rlnOriginY #15\n\
_rlnClassNumber #16\n\
_rlnNormCorrection #17\n\
_rlnRandomSubset #18\n\
_rlnLogLikeliContribution #19\n\
_rlnMaxValueProbDistribution #20\n\
_rlnNrOfSignificantSamples #21\n\
_rlnCoordinateX #22\n\
_rlnCoordinateY #23\n")

    k=np.pi/180.0
    for item in groups:
        j = imageGroup[item[0]]
        (rot,tilt,psi) = np.array([float(j[rot_index])*k,float(j[tlt_index])*k,float(j[psi_index])*k],dtype=np.float)
        t = np.array([np.cos(psi),-np.sin(psi)],dtype=np.float)*np.sin(tilt) * 350 + 512

        coordX=str(t[0]-float(j[orgX_index])*2)
        coordY=str(t[1]-float(j[orgY_index])*2)
        
        j[mic_index]=coordName.split('.')[0]+".mrc" 
        j[dU_index]=str(float(j[dU_index])-np.cos(tilt)*550)
        j[dV_index]=str(float(j[dV_index])-np.cos(tilt)*550)
        #print(j)
        j[orgY_index]="0.0"
        j[orgX_index]="0.0"
        #orginal_coordX=float(j[0]) + (float(coordX)-640)
        #rrginal_coordY=float(j[1]) + (float(coordY)-640)
        #print(j)
        if True:#orginal_coordX > 100 and orginal_coordX < 3718 and orginal_coordY > 100 and orginal_coordY< 3610:
            #j[0] = coordX
            #j[1] = coordY
            for item in j:
              
                coord.write(item+" ")
            coord.write(coordX+" "+coordY)
            #print(coordX+" "+coordY)
            coord.write('\n')
    coord.close()


if __name__=='__main__':
    root_name="run1_ct14_it029_data"
    from subprocess import call
    s="relion_particle_symmetry_expand --i {}.star --o  {}_expanded.star --sym I3".format(root_name, root_name)
    #call(s,shell=True)

    forg=open("{}_expanded.star".format(root_name),'r')
    fo = forg.readlines()
    forg.close()
    i=0

    o=len(fo)

    head_length=26

    for line in fo:
        i=i+1
        if i < head_length:
            pass
        elif i == head_length:
            l=line.split()
            imageGroup =[l]
        else:
            l=line.split()
            if len(l)>0 and imageGroup[0][img_index] == l[img_index]:
                imageGroup.append(l)

                if i == o:
                    handleGroup(imageGroup)
            else:
                handleGroup(imageGroup)
                imageGroup=[l]


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
