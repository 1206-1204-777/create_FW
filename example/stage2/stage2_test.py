import cupy as np
from stage2 import *
import weakref

# 動作実験
x0 = Variable(np.array(50.0))
x1 = Variable(np.array(2.0))

y = x0 + x1
y.backward()
print(x0.grad, x1.grad)