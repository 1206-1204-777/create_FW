import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import weakref
import numpy as np
import dezero as F
x0 = F.Variable(np.array([[[4, 5, 6], [5, 6, 7], [7, 8, 9]]]))
print(x0,"\n")
x1 = x0.T
y = F.cos(x1)
y = y.backward(create_graph=True)
print(x0.grad.reshape(9,1))
x2 = x0.transpose((1, 2, 0))
print (x2.data)