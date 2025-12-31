import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest
import numpy as np
from example.stage2.stage2 import Variable

class TestVariable(unittest.TestCase):
    def test_init(self):
        data = np.array(1.0)
        v = Variable(data)
        self.assertEqual(v.data, 1.0)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            Variable([1, 2, 3])

    def test_clearngrad(self):
        v = Variable(np.array(1.0))
        v.grad = np.array(1.0)
        v.crearngrad()
        self.assertIsNone(v.grad)

if __name__ == '__main__':
    unittest.main()