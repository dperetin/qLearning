#!/usr/bin/python

import random
import sys
import math


def generiraj(size, cilj, tip='gusta', raspon=(0, 0)):
    """
    size  - broj stanja u dijagramu
    cilj  - index ciljnog cvora, brojeci od nule. Nagrada je automatski postavljena na 100
    tip   - tip matrice koja se generira.     
            'gusta' - <default>
                      stanja mogu biti povezana sa svim stanjima, ali je mala vjerovatnost
                      da bude povezana sa stanjima koja su daleko
            'duga'  - stanja mogu biti povezana samo sa nekoliko najblizih stanja
    raspon - ureden par cijelih brojeva (a, b) 
            vrijedonsti matrice a su iz segmenta [a, b] 

    Funkcija vraca matricu nagrada sljedeceg formata:
         - ako stanja x i y nisu spojena, m(x, y) = -inf
         - ako jesu spojena, m(x, y) = z iz [a, b]
    """
    matrica = []
    
    #popunjavam matricu sa -inf
    for i in range(size):
        redak = []
        for j in range(size):
            redak.append(float('-inf'))
        matrica.append(redak)
     
    broj_elementa = random.sample(range(1, 3), 1);
    if tip == 'gusta':
        puni_elementi = random.sample(range(size), broj_elementa[0])
    if tip == 'duga':
        puni_elementi = random.sample(range(1, 8), broj_elementa[0])
    for j in puni_elementi:
            matrica[0][j] = random.randint(raspon[0], raspon[1]) 
            matrica[j][0] = matrica[0][j]
    
    for  i in range(1, size):
        broj_elementa = random.sample(range(1, 3), 1);
        if tip == 'gusta':
            puni_elementi = random.sample(range(i + 1), min(broj_elementa[0], size - i - 1))
        if tip == 'duga':
            puni_elementi = random.sample(range(i + 1, min(i+8, size)), min(broj_elementa[0], size - i - 1))
        elementi_prije = random.sample(range(max(i-2, 0), i), 1)
        for j in elementi_prije:
            matrica[i][j] = random.randint(raspon[0], raspon[1]) 
            matrica[j][i] = matrica[i][j]
        for j in puni_elementi:
            matrica[i][j] = 0
            matrica[j][i] = matrica[i][j]
    
    for i in range(size):
        matrica[i][i] = float('-inf')

    matrica[cilj][cilj] = 100

    for i in range(size):
        if matrica[i][cilj] != float('-inf'):
            matrica[i][cilj] = 100

    return matrica
   
   
def ToString(matrica):
    """
    Sprema matricu u jedan string, redovi su odvojeni znakom '\n', a 
    elementi reda zarezom
    """
    f = ','.join(map(lambda s: str(s), redak)) + '\n'


def AdjMat(matrica):
    """
    Iz matrice generira matricu susjeda koja se moze koristit za crtanje 
    grafova softverima kao sto su SAGE ili Mathematica.
    """
    dobra_matrica = []

    for redak in matrica:
        dobri_redak=[]
        for broj in redak:
            if broj == float('-inf'):
                dobri_redak.append(0)
            else:
                dobri_redak.append(1)
        dobra_matrica.append(dobri_redak)

    return dobra_matrica

    
def dobri(red):
    ret = []
    for i in range(0, len(red)):
        if red[i] != float('-inf'):
            ret.append(i)
    return ret


def parsiraj(cijeliFajl):
    """
    Iz stringa koji sadrzi informacije o dijagramu stanja, koji je spremljen 
    kao niz vrijednosti odvojenih zarezom, a redovi su odvojeni znakom '\n', 
    generira se matrica koja se moze korisiti za ucenje.
    """
    R = [map(lambda x: float(x), s.split(',')) for s in cijeliFajl.split()]
    return R


def imp(x, n=7):
    """
    Improved Matrix Print (tm)
    Ispisuje matricu u oku ugodnom formatu.
    """
    for red in x:
        print '\t'.join(map(lambda s: str(s)[:n], red))


def LearnQ(R, gamma, kraj, bench=False):
    """
    Vraca matricu Q
    
    R     - matrica nagrada
    gamma - koeficient
    kraj  - ciljni cvor, brojeci od 0
    bench - False <default>  
            True  - uz matricu Q vraca i broj izvrsenih epizoda i broj koraka algoritma
                    kao uredjenu trojku
    """   
    size = len(R)
    
        
    # inicijaliziram Q na 0
    Q = []
    for red in R:
        qr = []
        for broj in red:
            qr.append(0.0)
        Q.append(qr)

    
    broj_epizoda = 0
    broj_koraka = 0
    
    while abs(Q[kraj][kraj] - 100/(1-gamma)) > 0.00001:  
        broj_epizoda += 1
        s = random.randint(0, size - 1)
        while True:
            broj_koraka += 1
            indeks = dobri(R[s])
            if len(indeks) == 0:
                break
            r = random.choice(indeks)
            Q[s][r] = R[s][r] + gamma * max(Q[r])
            if s == kraj: 
                break
            s = r
    if bench:
        return (Q, broj_epizoda, broj_koraka)
    return Q


def FindPath(Q, poc, kraj):
    """
    Vraca listu cvorova koji tvore najkraci put od cvora poc do cvora kraj, prema
    matrici Q.
    
    Q    - matrica Q
    poc  - pocetni cvor, brojeci od 0
    kraj - ciljni cvor, brojeci od 0
    """
    size = len(Q)
    # racuna najbolji put
    put = []
    put.append(poc)  
    s = poc
    while s != kraj:
        s = Q[s].index(max(Q[s]))
        put.append(s)
    return put
    
    
