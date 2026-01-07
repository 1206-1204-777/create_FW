import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import cupy as np
from dezero.core_simple import *
import weakref

# 動作実験
x0 = Variable(np.array(5.0))

y = x0 ** 2 
y.backward()
print(y.data)
print(-x0)
print(x0.grad)