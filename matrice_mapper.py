#!/usr/bin/env python
import sys
#--------------------------------------------------------------------------
# size of matrix A and B need to be specified
row_A,col_A,row_B,col_B=5,10,10,3
# to get size of A and B
# the matrix is defined as: A, row i,colomun j, value A[i,j]

for line in sys.stdin:
    key=line.split(',')

    matrix=key[0]
    row=int(key[1])
    col=int(key[2])
    value=float(key[3])
#for each element (i,j) of A emit (i,k),A[i,j] for k in 1...number of colomun of B 
#for each element (j,k) of B emit (i,k),B[j,k] for i in 1...number of line of A   
    if matrix=="A":
	for i in range(0,col_B):
	    key2= str(row)+","+ str(i)
	    print( '{0} {1} {2} '.format(key2,col,value))
    else:
	for j in range(0,row_A):
	    key2= str(j)+"," +str(col)
	    print( '{0} {1} {2}'.format(key2,row,value))
   # print(key2,row,value)

