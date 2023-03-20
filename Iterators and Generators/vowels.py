class vowels:

    def __init__(self, string: str):
        self.string = [letter for letter in string if letter.lower() in ('a', 'e', 'i', 'o', 'u', 'y')]
        self.start = 0
        self.end = len(self.string)

    def __iter__(self):
        return self

    def __next__(self):
        ind = self.start

        if self.start == self.end:
            raise StopIteration

        self.start += 1

        return self.string[ind]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)