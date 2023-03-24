import unittest
from validator import validateNumber, validateOperator
from exceptions.NotANumberException import NotANumber
from exceptions.InvalidOperatorException import InvalidOperator


class TestValidator(unittest.TestCase):
    def test_when_number_is_integer_then_return_integer(self):
        self.assertEqual(validateNumber('1'), 1)

    def test_when_number_is_float_then_return_float(self):
        self.assertEqual(validateNumber('1.0'), 1.0)

    def test_when_number_is_string_then_return_float(self):
        self.assertEqual(validateNumber('1.0'), 1.0)

    def test_when_number_is_string_then_return_float(self):
        self.assertEqual(validateNumber('1.0'), 1.0)

    def test_when_number_is_text_then_raise_exception(self):
        with self.assertRaises(NotANumber):
            validateNumber('a')

    def test_when_number_is_empty_then_raise_exception(self):
        with self.assertRaises(NotANumber):
            validateNumber('')

    def test_when_operator_is_plus_then_return_plus(self):
        self.assertEqual(validateOperator('+'), '+')

    def test_when_operator_is_minus_then_return_minus(self):
        self.assertEqual(validateOperator('-'), '-')

    def test_when_operator_is_multiply_then_return_multiply(self):
        self.assertEqual(validateOperator('*'), '*')

    def test_when_operator_is_divide_then_return_divide(self):
        self.assertEqual(validateOperator('/'), '/')

    def test_when_operator_is_text_then_raise_exception(self):
        with self.assertRaises(InvalidOperator):
            validateOperator('a')

    def test_when_operator_is_empty_then_raise_exception(self):
        with self.assertRaises(InvalidOperator):
            validateOperator('')


if __name__ == '__main__':
    unittest.main()
