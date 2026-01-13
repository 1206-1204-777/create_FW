import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import weakref
import cupy as np
from dezero.core_simple import *
from dezero.test_function import *
import contextlib
from dezero.util import *

x0 = Variable(np.array(0.0))
x1 = Variable(np.array(0.0))

z = rosenbrock(x0, x1)
print(z.data)
z.backward()
print(x0.grad, x1.grad)

plot_dot_graph(z, to_file='rosenbrock.png')