import arithmetic
import unittest
# Testing add_numbers function from arithmetic.
class Test_addition(unittest.TestCase):
	# Testing Integers
	def test_add_numbers_int(self):
		sum = arithmetic.add_numbers(50, 50)
		self.assertEqual(sum, 100)

	# Testing Floats
	def test_add_numbers_float(self):
		sum = arithmetic.add_numbers(50.55, 78)
		self.assertEqual(sum, 128.55)

	# Testing Strings
	def test_add_numbers_strings(self):
		sum = arithmetic.add_numbers('hello','python')
		self.assertEqual(sum, 'hellopython')

class Test_subtraction(unittest.TestCase):
	# Testing Integers
	def test_sub_numbers_int(self):
		diff = arithmetic.sub_numbers(50, 50)
		self.assertEqual(diff, 0)

	# Testing Floats
	def test_sub_numbers_float(self):
		diff = arithmetic.sub_numbers(80.00, 78)
		self.assertEqual(diff, 2.00)

class Test_multiplication(unittest.TestCase):
	# Testing Integers
	def test_mul_numbers_int(self):
		multi = arithmetic.mul_numbers(78, 46)
		self.assertEqual(multi, 3588)

	# Testing Floats
	def test_mul_numbers_float(self):
		multi = arithmetic.mul_numbers(77.85, 8)
		self.assertEqual(multi, 622.8)

class Test_division(unittest.TestCase):
	# Testing Integers
	def test_div_numbers_int(self):
		quotient = arithmetic.div_numbers(78, 2)
		self.assertEqual(quotient, 39)

	# Testing Floats
	def test_div_numbers_float(self):
		quotient = arithmetic.div_numbers(77.8, 2)
		self.assertEqual(quotient, 38.9)

if __name__ == '__main__':
	unittest.main()
