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

    def test_ecart_int(self):
        self.assertEqual(funcs.ecart_int([1,2,3,4]),1.25)
        self.assertEqual(funcs.ecart_int([0,0,0,0]),0)
        self.assertEqual(funcs.ecart_int([-1,-5,-4,-8]),6.25)
        self.assertEqual(funcs.ecart_int([8,-3,11,0]),32.5)

    def test_si_geo_int(self):
        self.assertEqual(funcs.si_geo_int([2,8,32,128]),True)
        self.assertEqual(funcs.si_geo_int([-7,-2,-8,-3]),False)
        self.assertEqual(funcs.si_geo_int([-1,-2,-4,-8]),True)
        self.assertEqual(funcs.si_geo_int([8,3,11,0]),False)

    def test_si_arith_int(self):
        self.assertEqual(funcs.si_arith_int([2,4,6,8]),True)
        self.assertEqual(funcs.si_arith_int([-7,-2,-8,-3]),False)
        self.assertEqual(funcs.si_arith_int([-1,0,1,2]),True)
        self.assertEqual(funcs.si_arith_int([8,3,11,0]),False)

    def test_geo_int(self):
        self.assertEqual(funcs.geo_int(2,[2,8,32,128]),(True,[512,2048]))
        self.assertEqual(funcs.geo_int(5,[-7,-2,-8,-3]),(False,None))
        self.assertEqual(funcs.geo_int(4,[-1,-2,-4,-8]),(True,[-16,-32,-64,-128]))
        self.assertEqual(funcs.geo_int(6,[8,3,11,0]),(False,None))
    
    def test_arith_int(self):
        self.assertEqual(funcs.arith_int(4,[2,4,6,8]),(True,[10,12,14,16]))
        self.assertEqual(funcs.arith_int(6,[-7,-2,-8,-3]),(False,None))
        self.assertEqual(funcs.arith_int(3,[-1,0,1,2]),(True,[3,4,5]))
        self.assertEqual(funcs.arith_int(1,[8,3,11,0]),(False,None))

if __name__ == '__main__':
        unittest.main()

