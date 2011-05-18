#!/usr/bin/python

import random
import sys

def imp(x, n=7):
    for red in x:
        print '\t'.join(map(lambda s: str(s)[:n], red))

size = int(sys.argv[1])
matrica = []
cilj = int(sys.argv[2])

for i in range(size):
    redak = []
    for j in range(size):
        redak.append(random.random()*100)
    matrica.append(redak)

for  i in range(size):
    broj_elementa = random.sample(range(size-6, size-2), 1);
    prazni_elementi = random.sample(range(size), broj_elementa[0])
    for j in prazni_elementi:
        matrica[i][j] = float('-inf')

for i in range(size):
    for j in range(i, size):
        matrica[i][j] = matrica[j][i]

for i in range(size):
    matrica[i][i] = float('-inf')

matrica[cilj][cilj] = 100

for i in range(size):
    if matrica[i][cilj] != float('-inf'):
        matrica[i][cilj] = 100

imp(matrica)   

f = open('totalni_random.mat', 'w')

for redak in matrica:
    f.write(','.join(map(lambda s: str(s), redak)))
    f.write('\n')

dobra_matrica = []

for redak in matrica:
    dobri_redak=[]
    for broj in redak:
        if broj == float('-inf'):
            dobri_redak.append(0)
        else:
            dobri_redak.append(broj)
    dobra_matrica.append(dobri_redak)


g = open(r'q_learning_wolfram.mat', 'w')
wolfram = ""
wolfram += '{'
for redak in dobra_matrica:
    wolfram += '{'
    wolfram += ','.join(map(lambda s: str(s), redak))
    wolfram += '},'
g.write(wolfram[:-1]+'}')
