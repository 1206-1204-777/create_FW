import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import weakref
import cupy as np
from dezero.core_simple import *
from dezero.test_function import *
import contextlib
from dezero.util import *

x0 = Variable(np.array(2.0))

iters = 10
for i in range(iters):
    print(i, x0)
    z = f(x0)
    
    x0.crearngrad()
    z.backward()

    x0.data -= x0.grad / gx2(x0.data)

plot_dot_graph(z, to_file='newton.png')