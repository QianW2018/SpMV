#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

#CSR format
A = np.array([[1,0,0,0,0],[0,0,2,0,3],[0,4,0,0,5],[0,0,6,0,0],[0,0,0,7,0],[0,0,0,0,8]])
B = np.array([[1],[2],[3],[4],[5]])


rowNum = int(A.shape[0])
columnNum = int(A.shape[1])
Value = np.array([], dtype = int)
Column = np.array([], dtype = int)
RowPtr = np.array([], dtype = int)
Result = np.array([], dtype = int)


for i in range(rowNum):
    flag = 1;
    for j in range(columnNum):
        if A[i][j] != 0:
           Value = np.append(Value, np.array(A[i][j]))
           Column = np.append(Column, j)
           if flag == 1:
               RowPtr = np.append(RowPtr, len(Value)-1)
               flag = 0;

RowPtr = np.append(RowPtr, 8)

print (Value)
print (Column)
print (RowPtr)


#CSR kernel: A x B
for i in range(rowNum):
    start = int(RowPtr[i])
    end = int(RowPtr[i + 1])
    temp = 0
    for j in range(start, end):
        k = int(Column[j])
        temp += Value[j] * B[k][0]
    Result = np.append(Result, temp)


print (Result)
