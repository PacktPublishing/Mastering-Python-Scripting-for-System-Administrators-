class Student:
	def __init__(self, std):
		self.count = std

	def print_std(self):
		for i in range(self.count):
			print(i)
		return
if __name__ == '__main__':
	Student(5).print_std()

