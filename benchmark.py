#!/usr/bin/python

import qlearning as QL


graf = []
k=0.1
for i in range(20):
    print i
    se = 0
    sk = 0
    x = QL.generiraj(100, 99)
    a = QL.qLearning(x, k, 0, 99, bench=True)
    se += a[2]
    sk += a[3]
    graf.append((k, se, sk))
    QL.imp(graf)
    k+=0.05
 

QL.imp(graf)
