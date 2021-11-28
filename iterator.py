class CustomIterator:
    """
    Custom iterator class
    """
    def __next__(self):
        # custom implementation of next method
        if self.item < 10:
            self.item += 1
        else:
            raise StopIteration
        return self.item

    def __iter__(self):
        # custom implementation of iter method
        self.item = 0
        return self


my_iter = iter(CustomIterator())
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
