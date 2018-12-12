numbers = [10, 20, 30, 40]
numbers_iter = iter(numbers)
print(next(numbers_iter))
print(next(numbers_iter))
print(numbers_iter.__next__())
print(numbers_iter.__next__())
next(numbers_iter)
