import unittest
from ipynb.fs.full.Python_testcode import *
class TestStringMethods(unittest.TestCase):

# test function to test equality
     def test_Env_create(self):
        file= "Asia Prod.csv"
        actual = Env_create(file)
        expected = "Asia Prod"
        self.assertEqual(actual, expected

if __name__ == '__main__':
   unittest.main(argv=['first-arg-is-ignored'], exit=False)
