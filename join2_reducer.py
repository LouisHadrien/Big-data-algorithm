#!/usr/bin/env python
import sys

# imput from the mapper are: show,number of view or show,ABC (name of Channel)
show = None #initialize these variables
prev_show=  None
count= 0
for line in sys.stdin:
    line = line.strip() #strip out carriage return
    key_value = line.split(' ') #split line, into key and value, returns a list
    show=key_value[0] # name of TV show 
    value=key_value[1] # channel ABC or count of view
    #print(show,value)
    if show!= prev_show:
	    count=int(value)
	    prev_show=show
    else:
	if value.isdigit(): # check if it is ABC or number of view
	    count+=int(value)3 # sum view for a same show
	    prev_show=show
	else:
	    if value=='ABC':
		print('{0} {1}'.format(show,count))	
	    count=0
	    prev_show=show
