import unittest
import bmi

class Testbmi(unittest.TestCase):

    def test_height(self):
        result= bmi.height(5,8)
        self.assertEqual(result,68)



if __name__ == '__main__':
    unittest.main()
