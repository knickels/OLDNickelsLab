# Creates an n x n matrix filled with 'ones' and then plots
# Not the neatest way, but it works
# 1 goes to grey, which means unmapped. 0 is clear ground(white), 2 is obstacle (black)
 
import numpy as np
from pylab import *

n = 1000 # For an n x n matrix
np.random.seed(10)    
a=np.random.randint(1,2, size=(n, n))

mat=matshow(a, cmap=cm.binary, vmin=0, vmax=2)
colorbar(mat)
show()
