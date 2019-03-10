#!/usr/bin/env python
import sys


import sys
prev_index=0
prev_value=0
prev_key=0
somme=0
i=0
# make the dot product for each key (i,k)
for line in sys.stdin:
    item=line.split(" ")
    #print (item[0])
    key=item[0]
    index=item[1]
    value=item[2]
    if i==0: # deal with first line
	prev_value=value
	prev_index=index
	prev_key=key
	i=i+1
    else:
        if prev_key== key: 
            if prev_index==index: # compute dot product when applicable
	        somme+=float(prev_value)*float(value)
	    prev_index=index
	    prev_value=value
	    prev_key=key
        else:
	    print('{0} {1}'.format(prev_key,somme))
	    somme=0
	    prev_value=value
	    prev_index=index
	    prev_key=key
	
print('{0} {1}'.format(prev_key,somme)) # print last term	
    

