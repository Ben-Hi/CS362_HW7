import unittest
import fizzBuzz

class Test_FizzBuzz(unittest.TestCase):
    #Confirm that fizzBuzz prints integers 1-100 aside from the special fizz/buzz cases
    def test_print_to_100(self):
        output = fizzBuzz.fizzBuzz()
        for i in range(1, 101):
            if i % 3 != 0 and i % 5 != 0:
                self.assertEqual(output[i - 1], i)

    #Confirm that fizzBuzz prints 'Fizz' only for multiples of 3
    def test_print_fizz(self):
        output = fizzBuzz.fizzBuzz()
        for i in range(1, 101):
            if i % 3 == 0 and i % 5 != 0:
                self.assertEqual(output[i - 1], 'Fizz')

    def test_print_buzz(self):
        output = fizzBuzz.fizzBuzz()
        for i in range(1, 101):
            if i % 3 != 0 and i % 5 == 0:
                self.assertEqual(output[i - 1], 'Buzz')

if __name__ == '__main__':
    unittest.main()