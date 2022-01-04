import bibli
import unittest

class TestFuncs(unittest.TestCase):

    def test_min_int(self):
        self.assertEqual(bibli.create_db(), True)
        self.assertEqual(bibli.checkdata(), True)
        self.assertEqual(bibli.check_all_data(), None)
        #self.assertEqual(bibli.delete_table(), True)

if __name__ == '__main__':
        unittest.main()