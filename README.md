# casio_graph
A graphing environment for the Casio fx-CG50 calculator

Draw a graph from micropython.

To use it, do this:

from graph import *

def func(x):
  return sin(x)+sin(3*x)/3

g=Graph()
g.graph(func,xmin=-20,xmax=20)

Note that this package relies on the casioplot package which was added to version 3.40 of the OS. If you're on an older version, you'll need to update: https://edu.casio.com/download/index.php

-- 4dc5.com
