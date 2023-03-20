class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        n = self.start

        if self.count == 0:
            raise StopIteration

        self.start += self.step
        self.count -= 1

        return n


numbers = take_skip(10, 5)
for number in numbers:
    print(number)