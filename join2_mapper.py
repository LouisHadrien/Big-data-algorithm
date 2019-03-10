#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
for line in sys.stdin:
    line = line.strip() #strip out carriage return
    key_value = line.split(",") #split line, into key and value, returns a list
    key_in = key_value[0] #key is first item in list
    value_in = key_value[1] #value is 2nd item
 #print key_in
    if value_in=="ABC":
        print( '{0} {1}'.format(key_in,value_in) ) 
    else: #key is only <word> so just pass it through
	if value_in.isdigit():
	    print( '{0} {1}'.format(key_in,value_in) ) 
       
