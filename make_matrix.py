#!/usr/bin/env python
import sys
from random import *
import numpy as np

# create a matrix in a file text
# choose number of line and column
# columns are seperated by commas

m=5 # line A
n=10 # column A line B
p=3#column B
matA=[]
for i in range(m):
    for j in range(n):
	coef=randint(-10,10)
	matA+=[["A",i,j,coef]]

matB=[]
for k in range(n):
    for l in range(p):
	coef=randint(-10,10)
	matB+=[["B",k,l,coef]]

mat=matA+matB
#print(mat)
np.savetxt("/home/cloudera/Desktop/matrix.txt",mat,delimiter=',',fmt="%s")

