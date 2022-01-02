import funcs
import unittest

class TestFuncs(unittest.TestCase):

    def test_min_int(self):
        self.assertEqual(funcs.min_int(0,2),0)
        self.assertEqual(funcs.min_int(-1,-5),-5)
        self.assertEqual(funcs.min_int(-1,2),-1)
        self.assertEqual(funcs.min_int(0,0),0)

    def test_moy_int(self):
        self.assertEqual(funcs.moy_int([0,1,2,3]),1.5)
        self.assertEqual(funcs.moy_int([-1,-5,-12]),-6)
        self.assertEqual(funcs.moy_int([-5,1,-2,3]),-0.75)
        self.assertEqual(funcs.moy_int([0,0,0,0]),0)

if __name__ == '__main__':
        unittest.main()

