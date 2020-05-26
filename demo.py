from graph import *

def func(x):
  return sin(x)+sin(3*x)/3

g=Graph()
g.graph(func,xmin=-20,xmax=20)
