from casioplot import *
from math import *

# Draw a graph.
#
# To use it, do this:
#
# from graph import *
#
# def func(x):
#  return sin(x)+sin(3*x)/3
#
# g=Graph()
# g.graph(func,xmin=-20,xmax=20)

class Graph:

  def graph(self,fn,xmin=-5.0,xmax=5.0,color=(0,0,0)):
    # Lists of x values and y values
    xl=[]
    yl=[]

    # Set graph edges
    sxmin=20 # Left
    sxmax=383 # Right
    symin=0 # Top
    symax=171 # Bottom
    sxrange=sxmax-sxmin
    syvrange=symax-symin

    # Evaluate function for every x pixel
    for i in range(0,sxrange+1):
      x=i/sxrange * (xmax-xmin) + xmin
      xl.append(x)
      y=fn(x)
      yl.append(y)
      # Update min and max y values
      if i==0:
        ymin=y
        ymax=y
      if y<ymin:
        ymin=y
      if y>ymax:
        ymax=y

    # Edge case: if it's just constant y, make min and max y different
    if ymin==ymax:
      ymin-=1
      ymax+=1

    # Add a margin to top and bottom
    ymid=(ymin+ymax)/2
    ymax=(ymax-ymid)*1.05+ymid
    ymin=(ymin-ymid)*1.05+ymid

    yvrange=ymax-ymin
    xvrange=xmax-xmin

    # Draw vertical grid lines, using a heuristic to work out the intervals
    expt=floor(log10(xvrange))

    ex1=floor(xmin/10**expt)
    ex2=ceil(xmax/10**expt)

    for ex in range(ex1,ex2+1):
      x=ex*10**expt
      sx=int((x-xmin)/(xvrange)*sxrange)
      for sy in range(0,(syvrange+1)):
        set_pixel(sx+sxmin,sy,(127,127,127))
      draw_string(sx+sxmin,175,str(x))

    # Draw horizontal grid lines, using a heuristic to work out the intervals
    expt=floor(log10(yvrange))

    ex1=floor(ymin/10**expt)
    ex2=ceil(ymax/10**expt)

    for ex in range(ex1,ex2+1):
      y=ex*10**expt
      sy=int(syvrange-(y-ymin)/(yvrange)*syvrange)
      for sx in range(0,(sxrange+1)):
        set_pixel(sx+sxmin,sy,(127,127,127))
      draw_string(0,sy,str(y))

    # Plot the graph
    for sx in range(1,(sxrange+1)):
      # Calculate previous and current y values
      sy1=int(syvrange-(yl[sx-1]-ymin)/(yvrange)*syvrange)
      sy2=int(syvrange-(yl[sx]-ymin)/(yvrange)*syvrange)
      # Set step depending on whether curve is going up or down
      if sy1>sy2:
        st=-1
      else:
        st=1
      # Draw vertical line from previous y to current y (so we don't have gaps)
      for sy in range(sy1,sy2+st,st):
        self._point(sx+sxmin,sy,color)

    show_screen()

  # Draw a thick point
  def _point(self,x,y,color=(0,0,0)):
    set_pixel(x,y,color)
    set_pixel(x-1,y,color)
    set_pixel(x,y-1,color)
    set_pixel(x+1,y,color)
    set_pixel(x,y+1,color)
