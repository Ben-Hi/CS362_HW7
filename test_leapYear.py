import unittest
import leapYear

class Test_LeapYear(unittest.TestCase):
    def test_not_divisible_by_4(self):
        self.assertEqual(leapYear.leapYear(5), '5 is not a leap year')

    def test_div_by_100_not_400(self):
        self.assertEqual(leapYear.leapYear(500), '500 is not a leap year')

if __name__ == '__main__':
    unittest.main()