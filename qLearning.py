#!/usr/bin/python

import random
import sys

def dobri(red):
    ret = []
    for i in range(0,len(red)):
        if red[i] != float('-inf'):
            ret.append(i)
    return ret

def main():
  
    if len(sys.argv) != 4:
        print sys.argv[0], '<dat>', '<poc>', '<cilj>'
        print '\t<dat>  - ime datoteke u koju je spremljena ulazna matrica'
        print '\t<poc>  - pocetni cvor, moze biti bilo koji'
        print '\t<cilj> - ciljni cvor, mora biti u skladu s ulaznom matricom'
        sys.exit(1)
  
    filename = sys.argv[1]
    poc = int(sys.argv[2])
    kraj = int(sys.argv[3])
      
    # ucitavam matricu iz datoteke
    f = open(filename, 'rU')
    cijeliFajl = f.read()
    R = [map(lambda x: float(x), s.split(',')) for s in cijeliFajl.split()]
      
    # inicijaliziram Q na 0
    Q=[]
    for red in R:
        qr=[]
        for broj in red:
            qr.append(0.0)
        Q.append(qr)

    #inicijaliziram gammu
    gamma = 0.8
  
    # Q learning
    for i in range(1000):
        s = random.randint(0, kraj)
        while True:
            r = random.choice(dobri(R[s]))
            Q[s][r] = R[s][r] + gamma * max(Q[r])
            if s == kraj: 
                break
            s = r
  
    # ispis matrice Q
    print    
    print 'Matrica Q:'  
    for red in Q:
        print '\t'.join(map(lambda n: str(n)[:7], red))
  
    # racuna najbolji put
    put = []  
    s = poc
    while s != kraj:
        s = Q[s].index(max(Q[s]))
        put.append(s)
  
    # ispis puta
    print
    print 'Najkraci put'
    print ' -> '.join(map(str, put))
    print
  
if __name__=='__main__':
    main()
