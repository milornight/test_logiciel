import bibli
import unittest

class TestFuncs(unittest.TestCase):

    def test_min_int(self):
        self.assertEqual(bibli.checkdata(), True)
        self.assertEqual(bibli.check_all_data(), None)

if __name__ == '__main__':
        unittest.main()