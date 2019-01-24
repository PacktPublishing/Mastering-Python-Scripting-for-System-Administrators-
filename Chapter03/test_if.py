import if_example
import unittest

class Test_if(unittest.TestCase):
	def test_if(self):
		result = if_example.check_if()
		self.assertEqual(result, 100)
		
if __name__ == '__main__':
	unittest.main()

