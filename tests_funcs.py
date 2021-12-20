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

    def test_med_int(self):
        self.assertEqual(funcs.med_int([2,2,2,2]),2)
        self.assertEqual(funcs.med_int([1,2,3]),2)
        self.assertEqual(funcs.med_int([6,4,5,7]),5.5)
        self.assertEqual(funcs.med_int([8,-3,11]),8)
        self.assertEqual(funcs.med_int([1,5,3,9,10,7]),6)

if __name__ == '__main__':
        unittest.main()

