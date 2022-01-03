import bibli
import unittest

class TestFuncs(unittest.TestCase):

    def test_min_int(self):
        
        self.assertEqual(bibli.checkdata(), True)
        self.assertEqual(bibli.check_all_data(), None)
        #self.assertEqual(bibli.min_int(-1,2),-1)
        #self.assertEqual(bibli.min_int(0,0),0)

if __name__ == '__main__':
        unittest.main()