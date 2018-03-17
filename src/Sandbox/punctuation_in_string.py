"""
Created on ???

Used to answer this question:
???

@author: physicalattraction
"""

import string

invalidChars = string.punctuation


def judge_words(words):
    for word in words:
        if any(char in invalidChars for char in word):
            print('{} contains punctuation: {}'.format(word, ''.join(find_invalid_chars(word))))
        else:
            print('{} does not contain punctuation'.format(word))


def find_invalid_chars(word):
    result = []
    for char in word:
        if char in invalidChars:
            result.append(char)
    return result


if __name__ == '__main__':
    word1 = 'hello'
    word2 = 'hello?'
    judge_words([word1, word2])

