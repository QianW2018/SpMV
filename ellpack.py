#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

#Ellpack format
A = np.array([[1,0,0,0,0],[0,0,2,0,3],[0,4,0,0,5],[0,0,6,0,0],[0,0,0,7,0],[0,0,0,0,8]])
B = np.array([[1],[2],[3],[4],[5]])


rowNum = int(A.shape[0])
columnNum = int(A.shape[1])
count = np.array([], dtype = int)
r = 0

for i in range(rowNum):
    count = np.append(count, 0)
    for j in range(columnNum):
        if A[i][j] != 0:
            count[i] += 1
count = max(count)


NonZerosEntries = [[0 for i in range(count)] for j in range(rowNum)]
Column = [[-1 for i in range(count)] for j in range(rowNum)]
Result = np.array([])


for i in range(rowNum):
    c = 0
    for j in range(columnNum):
        if A[i][j] != 0:
            NonZerosEntries[r][c] = A[i][j]
            Column[r][c] = j
            c += 1
    r += 1


#Ellpack kernel

for i in range(rowNum):
    temp = 0
    for j in range(count):
        if Column[i][j] == -1:
            break
        else:
            temp += NonZerosEntries[i][j] * B[Column[i][j]]
    Result = np.append(Result, temp)

print (Result)
