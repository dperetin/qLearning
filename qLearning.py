#!/usr/bin/python

import random

def dobri(red):
  ret = []
  for i in range(0,len(red)):
    if red[i] != float('-inf'):
      ret.append(i)
  return ret

def main():
  f = open('R.mat', 'rU')
  cijeliFajl = f.read()
  R = [map(lambda x: float(x), s.split(',')) for s in cijeliFajl.split('\n')]
  #print R
  
  q=[]
  for red in R:
    qr=[]
    for broj in red:
      qr.append(0.0)
    q.append(qr)

  gamma = 0.8
  for i in range(1000):
    s = random.randint(0, 5)
    while True:
        r = random.choice(dobri(R[s]))
        q[s][r] = R[s][r] + gamma * max(q[r])
        if s == 5: break
        s = r
  for red in q:
    print red
    
  s = 2
  while s != 5:
    s = q[s].index(max(q[s]))
    print s
  
if __name__=='__main__':
  main()
