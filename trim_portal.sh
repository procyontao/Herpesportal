
cat  ../bin1/particles_run8_cls1_removedup.star | grep particles | while read line;
do 
    i=`echo $line | awk '{print $1}' | awk -F '@' '{print $1}'`
    trimvol -z $i,$i ../bin1/particles_vertices_stack.mrcs particles_portal/1$i".mrc"
done
