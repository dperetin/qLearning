#!/usr/bin/python

import random
import qlearning as QL


graf = []
k=0.1
for i in range(100, 1000, 100):
    print i
    se = 0
    sk = 0
    cilj = random.randint(1, i-1);
    x = QL.generiraj(i, cilj, tip='duga')
    a = QL.qLearning(x, 0.8, random.randint(0,i-1), bench=True)
    se += a[2]
    sk += a[3]
    graf.append((i, se, sk))
    QL.imp(graf)

QL.imp(graf)
