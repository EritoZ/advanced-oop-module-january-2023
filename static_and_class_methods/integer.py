class Integer:

    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if type(float_value) is not float:
            return "value is not a float"

        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value: str):
        roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                        "D": 500, "M": 1000, "G": 5000, "H": 10000}
        converted_nums = []

        for n in value:
            conv_num = roman_values[n]

            if converted_nums and conv_num > converted_nums[-1]:
                last_number = converted_nums[-1]

                conv_num -= last_number * 2

            converted_nums.append(conv_num)

        sum_nums = sum(converted_nums)

        return cls(sum_nums)

    @classmethod
    def from_string(cls, value):
        if type(value) is not str:
            return "wrong type"

        return cls(int(value))


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))