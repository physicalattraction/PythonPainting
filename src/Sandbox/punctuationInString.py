import string

word1 = 'hello'
word2 = 'hello?'

invalidChars = string.punctuation

for word in (word1, word2):
    if any(char in invalidChars for char in word):
        print("{} contains punctuation".format(word))
    else:
        print("{} does not contain punctuation".format(word))

    def find_invalid_chars(word):
        result = []
        for char in word:
            if char in invalidChars:
                result.append(char)
        return result