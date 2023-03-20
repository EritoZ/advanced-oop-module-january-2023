class countdown_iterator:

    def __init__(self, count: int):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        n = self.count

        if self.count == -1:
            raise StopIteration

        self.count -= 1

        return n


iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")