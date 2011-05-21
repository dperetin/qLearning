#!/usr/bin/python

import random
import sys
import math

def imp(x, n=7):
    for red in x:
        print '\t'.join(map(lambda s: str(s)[:n], red))

def main():
    size = int(sys.argv[1])
    matrica = []
    cilj = int(sys.argv[2])

    
    #popunjavam matricu sa -inf
    for i in range(size):
        redak = []
        for j in range(size):
            redak.append(float('-inf'))
        matrica.append(redak)
     
    broj_elementa = random.sample(range(1, 3), 1);
    #puni_elementi = random.sample(range(1, 3), broj_elementa[0])
    puni_elementi = random.sample(range(size), broj_elementa[0])
    for j in puni_elementi:
            matrica[0][j] = 0
            matrica[j][0] = matrica[0][j]
    
    for  i in range(1, size):
        #print i
        broj_elementa = random.sample(range(1, 3), 1);
        #puni_elementi = random.sample(range(i + 1, min(i+3, size)), min(broj_elementa[0], size - i - 1))
        puni_elementi = random.sample(range(i + 1), min(broj_elementa[0], size - i - 1))
        elementi_prije = random.sample(range(max(i-2, 0), i), 1)
        for j in elementi_prije:
            matrica[i][j] = 0
            matrica[j][i] = matrica[i][j]
        for j in puni_elementi:
            matrica[i][j] = 0
            matrica[j][i] = matrica[i][j]
    

 #   for i in range(size):
  #      for j in range(i, size):
   #         matrica[i][j] = matrica[j][i]

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
                dobri_redak.append(1)
        dobra_matrica.append(dobri_redak)


    g = open(r'q_learning_wolfram.mat', 'w')
    wolfram = ""
    wolfram += '{'
    for redak in dobra_matrica:
        wolfram += '{'
        wolfram += ','.join(map(lambda s: str(s), redak))
        wolfram += '},'
    g.write(wolfram[:-1]+'}')
    
if __name__ == '__main__':
    main()
