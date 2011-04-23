#!/usr/bin/python

def main():
  f = open('R.mat', 'rU')
  cijeliFajl = f.read()
  R = [map(lambda x: float(x), s.split(',')) for s in cijeliFajl.split('\n')]
  print R
if __name__=='__main__':
  main()
