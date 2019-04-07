#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

#HYB format
A = np.array([[1,0,0,0,0],[0,0,2,3,1],[0,4,0,0,5],[0,0,6,0,0],[0,0,0,7,0],[0,0,0,0,8]])
B = np.array([[1],[2],[3],[4],[5]])


def hyb(matrix1, matrix2):
    rowNum = int(matrix1.shape[0])
    columnNum = int(matrix1.shape[1])
    reformatMatrix = [[0 for i in range(columnNum)] for j in range(rowNum)]
    count = np.array([], dtype = int)



    # reformat matrix
    for i in range(rowNum):
        c = 0
        for j in range(columnNum):
            if matrix1[i][j] != 0:
                reformatMatrix[i][c] = matrix1[i][j]
                c += 1
    reformatMatrix = np.array(reformatMatrix)


    # calculate matrix density and slice matrix
    for j in range(columnNum):
        count = np.append(count, 0)
        for i in range(rowNum):
            if reformatMatrix[i][j] != 0:
                count[j] += 1

    breakline = 0
    for i in range(len(count)):
        percTemp = float(count[i])/rowNum
        if percTemp < 0.3:
            breakline = i
            break


    #sliced matrix
    ellMatrix = reformatMatrix[..., 0:i]
    cooMatrix = reformatMatrix[..., i:]


    # calculate column indices for Ellpack
    column = [[-1 for i in range(breakline)] for j in range(rowNum)]
    r = 0
    for i in range(rowNum):
        c = 0
        for j in range(columnNum):
            if matrix1[i][j] != 0 and c < breakline:
                column[r][c] = j
                c += 1
        r += 1


    #Ellpack calculation
    ResultELL = np.array([], dtype = int)
    for i in range(rowNum):
        tempELL = 0
        for j in range(breakline):
                tempELL += ellMatrix[i][j] * matrix2[column[i][j]]
        ResultELL = np.append(ResultELL, tempELL)
    print("Ellpack result is:", ResultELL)


    #COO calculation
    ValueCOO = np.array([], dtype = int)
    ColumnCOO = np.array([], dtype = int)
    RowCOO = np.array([], dtype = int)
    tempCOO = [[0] for j in range(rowNum)]
    ResultCOO = np.array([], dtype = int)


    columnNumCOO = columnNum - breakline
    for i in range(rowNum):
        s = 0
        for j in range(columnNum):
            if matrix1[i][j] != 0:
                s += 1
                if s > breakline:
                    ValueCOO = np.append(ValueCOO, matrix1[i][j])
                    ColumnCOO = np.append(ColumnCOO, j)
                    RowCOO = np.append(RowCOO, i)


    for i in range(len(ValueCOO)):
        tempCOO[RowCOO[i]] += ValueCOO[i] * matrix2[ColumnCOO[i]]


    for i in range(len(tempCOO)):
        ResultCOO = np.append(ResultCOO, tempCOO[i])

    print ("COO result is:", ResultCOO)


    # COO plus ellpack

    Result = ResultCOO + ResultELL
    print ("HYB result is:", Result)



hyb(A, B)
