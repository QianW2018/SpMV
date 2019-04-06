#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from ellpack import ellpack
from coo import coo

#HYB format
A = np.array([[1,0,0,0,0],[0,0,2,3,1],[0,4,0,0,5],[0,0,6,0,0],[0,0,0,7,0],[0,0,0,0,8]])
B = np.array([[1],[2],[3],[4],[5]])


def hyb(matrix1, matrix2):
    rowNum = int(matrix1.shape[0])
    columnNum = int(matrix1.shape[1])
    reformatMatrix = [[0 for i in range(columnNum)] for j in range(rowNum)]
    count = np.array([], dtype = int)

    for i in range(rowNum):
        c = 0
        for j in range(columnNum):
            if matrix1[i][j] != 0:
                reformatMatrix[i][c] = matrix1[i][j]
                c += 1
    reformatMatrix = np.array(reformatMatrix)

    for j in range(columnNum):
        count = np.append(count, 0)
        for i in range(rowNum):
            if reformatMatrix[i][j] != 0:
                count[j] += 1

    for i in range(len(count)):
        percTemp = float(count[i])/rowNum
        if percTemp < 0.3:
            breakLine = i
            break

    ellMatrix = reformatMatrix[..., 0:i]
    cooMatrix = reformatMatrix[..., i:]
    coo(cooMatrix, matrix2)
    ellpack(ellMatrix, matrix2)


hyb(A, B)
