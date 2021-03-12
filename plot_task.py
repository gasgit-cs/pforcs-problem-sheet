
# program  to graph, plot and visualise
# author glen gardiner

import matplotlib.pyplot as plt
import numpy as np

# create x points
x =np.array(range(0,4))

# x, x*x, x*x*x
fx = x
gx = x**2
hx = x**3

# print arrays to console 
title = print("fx = {} gx = {} hx = {}".format(fx,gx,hx))

# plot fx, line width 1, dash-dot, red, points marked with *
plt.plot(x , fx, linewidth='1', ls='-.', color='r',  ms='5', marker='*')
# plot gx, line width 2, dotted, green, points marked with +
plt.plot(x , gx, linewidth='2', ls=':', color='g', ms='10', marker = '+')
# plot hx, line width 3, solid, yellow, points marked with circle, mark eredge color cyan
plt.plot(x , hx, linewidth='3', color='y', marker='o', ms='15',mec='c')

# labels
plt.xlabel("x")
plt.ylabel("*(x)")

# grid
plt.grid(color = 'c', linestyle = '--', linewidth = 0.3)

# title
plt.title('f(x)=x, g(x)=x2 and h(x)=x3 Range[0,4]')

# legend 
plt.legend(['fx', 'gx', 'hx'], loc ='upper left')

# save figure to png 
plt.savefig('plot_task.png')

# render the figure in gui loop
plt.show()


