def pt(l):
    for item in l:
        print item,
    print ""


def handleGroup(imageGroup):
    #print imageGroup
    if len(imageGroup)>10:
        pt(imageGroup)
        #pass
    else:
        maxScore=imageGroup[0][19]
        maxTmp=0
        for i in range(1,len(imageGroup)):
            #pt(imageGroup)
            if imageGroup[i][19] > maxScore:
                maxTmp=i
                maxScore=imageGroup[i][19]
        pt(imageGroup[maxTmp])


if __name__=='__main__':
    forg=open('./run1_cls5.star','r')
    fo = forg.readlines()
    i=0
    o=len(fo)

    for line in fo:
        i=i+1
        if i < 28:
            print line,
        elif i == 28:
            l=line.split()
            imageGroup =[l]
        else:
            l=line.split()

            if len(l)>0 and imageGroup[0][1] == l[1]:
                imageGroup.append(l)

                if i == o:
                    handleGroup(imageGroup)
            else:
                handleGroup(imageGroup)
                imageGroup=[l]
