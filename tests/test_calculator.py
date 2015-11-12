import math
import unittest
from calculator import Calculator


class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    """Add tests"""

    def test_add_of_ints(self):
        self.assertEqual(self.calculator.add(5, 1), 6)

    def test_commutativity_of_add_of_ints(self):
        self.assertEqual(self.calculator.add(1, 5), self.calculator.add(5, 1))

    def test_add_of_int_and_float(self):
        self.assertAlmostEqual(self.calculator.add(5, 3.22), 8.22)

    def test_commutativity_of_add_of_int_and_float(self):
        self.assertAlmostEqual(self.calculator.add(3.2, 5), self.calculator.add(5, 3.2))

    def test_add_of_floats(self):
        self.assertEqual(self.calculator.add(5.2, 1.2), 6.4)

    def test_commutativity_of_add_of_floats(self):
        self.assertEqual(self.calculator.add(1.2, 5.23), self.calculator.add(5.23, 1.2))

    def test_negative_add(self):
        self.assertNotEqual(self.calculator.add(3, 4), -7)

    """Subtract tests"""

    def test_subtract_of_ints(self):
        self.assertEqual(self.calculator.subtract(1, 5), -4)

    def test_subtract_of_int_and_float(self):
        self.assertAlmostEqual(self.calculator.subtract(5, 3.22), 1.78)

    def test_subtract_of_floats(self):
        self.assertEqual(self.calculator.subtract(5.3, 1.2), 4.1)

    def test_negative_subtract(self):
        self.assertNotEqual(self.calculator.subtract(4, 3), -1)

    """Multiply tests"""

    def test_multiply_of_ints(self):
        self.assertEqual(self.calculator.multiply(5, 2), 10)

    def test_commutativity_of_multiply_of_ints(self):
        self.assertEqual(self.calculator.multiply(2, 5), self.calculator.multiply(5, 2))

    def test_multiply_of_int_and_float(self):
        self.assertAlmostEqual(self.calculator.multiply(5, 3.21), 16.05)

    def test_commutativity_of_multiply_of_int_and_float(self):
        self.assertAlmostEqual(self.calculator.multiply(3.2, 5), self.calculator.multiply(5, 3.2))

    def test_multiply_of_floats(self):
        self.assertEqual(self.calculator.multiply(5.2, 1.2), 6.24)

    def test_commutativity_of_multiply_of_floats(self):
        self.assertEqual(self.calculator.multiply(1.2, 5.23), self.calculator.multiply(5.23, 1.2))

    def test_negative_multiply(self):
        self.assertNotEqual(self.calculator.multiply(3, 4), -7)

    """Divide tests"""

    def test_divide_of_ints(self):
        self.assertEqual(self.calculator.divide(5, -2), -2.5)

    def test_divide_of_int_and_float(self):
        self.assertAlmostEqual(self.calculator.divide(5, 3.2), 1.5625)

    def test_divide_of_floats(self):
        self.assertAlmostEqual(self.calculator.divide(5.4, 1.2), 4.5)

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, self.calculator.divide, 3, 0)

    def test_negative_divide(self):
        self.assertNotEqual(self.calculator.divide(3, 4), -7)

    """Sin tests"""

    def test_sin_of_zero(self):
        self.assertEqual(self.calculator.sin(0), 0)

    def test_sin_of_pi_div_2(self):
        self.assertEqual(self.calculator.sin(math.pi/2), 1)

    def test_sin_of_floats(self):
        self.assertLess(self.calculator.sin(5.4), 1)

    def test_negative_sin(self):
        self.assertNotAlmostEqual(self.calculator.sin(math.pi/6), 1)
