def palindrome(word, index):

    def reverse_word(word, index):
        if index == -len(word) + 1:
            return word[index - 1]

        return word[index - 1] + reverse_word(word, index - 1)

    if reverse_word(word, index) == word:
        return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"


print(palindrome("abcba", 0))

print(palindrome("peter", 0))