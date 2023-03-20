from collections import deque


class sequence_repeat:

    def __init__(self, sequence, number: int):
        self.sequence = deque(sequence)
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        letter = self.sequence[0]

        if self.number == 0:
            raise StopIteration

        self.number -= 1
        self.sequence.rotate(-1)

        return letter


result = sequence_repeat('I Love Python', 20)
for item in result:
    print(item, end ='')