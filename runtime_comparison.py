#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import time
from operator import itemgetter

from csr import csr
from ellpack import ellpack
from coo import coo
from hyb import hyb


A = np.array([[1,0,0,0,0],[0,0,2,0,3],[0,4,0,0,5],[0,0,6,0,0],[0,0,0,7,0],[0,0,0,0,8]])
B = np.array([[1],[2],[3],[4],[5]])


def runtime_comp(matrix):
    start1 = time.time()
    for i in range(100):
        csr(A, B)
    end1 = time.time()
    runtime_csr = end1 - start1


    start2 = time.time()
    for i in range(100):
        ellpack(A, B)
    end2 = time.time()
    runtime_ellpack = end2 - start2



    start3 = time.time()
    for i in range(100):
        coo(A, B)
    end3 = time.time()
    runtime_coo = end3 - start3


    start4 = time.time()
    for i in range(100):
        hyb(A, B)
    end4 = time.time()
    runtime_hyb= end4 - start4


    method = ["CSR", "Ellpack", "COO", "HYB"]
    runtime = [runtime_csr, runtime_ellpack, runtime_coo, runtime_hyb]
    minRuntime = min(runtime)
    minRuntimeIndex = min(enumerate(runtime), key=itemgetter(1))[0]
    bestAlg = method[minRuntimeIndex]


    print('Runtime of CSR is: %.4f' % runtime_csr)
    print('Runtime of Ellpack is: %.4f' % runtime_ellpack)
    print('Runtime of COO is: %.4f' % runtime_coo)
    print('Runtime of HYB is: %.4f' % runtime_hyb)
    print("The best algorithm with minimum runtime is:", bestAlg, "with 100x runtime of", minRuntime)


if __name__ == "__main__":
    runtime_comp(A)
