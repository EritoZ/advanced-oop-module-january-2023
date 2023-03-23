def vowel_filter(function):

    def wrapper():
        vowels = ['a', 'o', 'u', 'i', 'e']

        return [l for l in function() if l in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())