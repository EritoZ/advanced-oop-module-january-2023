class reverse_iter:

    def __init__(self, iterable: iter):
        self.iterable = iterable
        self.start = len(self.iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        ind = self.start

        if self.start == -1:
            raise StopIteration

        self.start -= 1

        return self.iterable[ind]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)