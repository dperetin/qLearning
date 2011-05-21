#!/usr/bin/python

import qlearning as QL


graf = []
for i in range(10, 100, 10):
	se = 0
	sk = 0
	for j in range(10):
		print i, j
		x = QL.generiraj(i, i-1)
		a = QL.qLearning(x, 0.8, 0, i-1, bench=True)
		se += a[2]
		sk += a[3]
	graf.append((se/10, sk/10))

QL.imp(graf)
