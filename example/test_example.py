import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import weakref
import cupy as np
from dezero.core_simple import *
from dezero.test_function import *
import contextlib

x0 = Variable(np.array(1.0))
x1 = Variable(np.array(1.0))

z = goldstein_price(x0, x1)
z.backward()
print(x0.grad, x1.grad)