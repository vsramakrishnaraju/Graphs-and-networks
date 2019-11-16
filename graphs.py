#!/usr/bin/env python
# coding: utf-8

# In[3]:


## Author: Venkata

import numpy
import random
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

#filename = "networkDatasets/toyN.txt"
filename = "toyN.txt"
X = numpy.loadtxt(filename)
n = max(max(X[:,0]),max(X[:,1]))
n = int(n)
A = numpy.zeros((n,n))
#remember python index the entries from 0 to n-1.
#populate A..iterate over X and populate entries in A
#Then calculate measures..

# adjacent matrix 

for i in range(len(X)):
    p = int(X[i][0]-1)
    q = int(X[i][1]-1)
    A[p][q] = 1
    A[q][p] = 1
    
# print(A)
# Degree 

degree = []
for i in range(len(A)):
    count = 0
    for j in range(len(A[0])):
        if (A[i][j] == 1):
            count = count+1
    degree.append(count)

# print(degree)

a = dict(Counter(degree))

j = list(a.keys())

k_j = list(a.values())

p_j = [x / n for x in k_j]

df = pd.DataFrame({'degree, j':j, 'probs of degree j':p_j, 'no .of nodes, k_j':k_j })

df.plot(x='degree, j', y='no .of nodes, k_j', kind = 'scatter',  title='Degree vs no. of nodes in k_j')

df.plot(x='degree, j', y='probs of degree j', kind = 'scatter', title='Degree vs probs of degree j', loglog=True, style='b')

# Clustring coeficient

edges = []
for i in range(len(A)):
    neig = []
    for j in range(len(A[0])):
        if(A[i][j] == 1):
            neig.append(j)
    
    ed = 0 
    for i in neig:
        for j in neig:
            if(A[i][j] == 1):
                ed = ed+1
    
    edges.append(int(ed/2))
    
# print(edges)
    
clust_coeff = []
for i in range(len(edges)):
    if(degree[i]>1):
        r = 2*(edges[i])
        s1 = degree[i]
        s2 = degree[i]-1
        clust = r/(s1*s2)
    else:
        clust = 0
    clust_coeff.append(clust)
    
# clustring coff of all nodes 

coeff = 0 
for i in clust_coeff:
    coeff = coeff +i
coeff_n = coeff/n
    
print('Final Clustering Coefficient', coeff_n)

