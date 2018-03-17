"""
Created on Mar 17, 2018

Used to answer this question:
https://stackoverflow.com/a/49335335/1469465

@author: physicalattraction
"""


def filter_items_between_strings(input: [str], separator: str):
    separator_indexes = [index for index, word in enumerate(input) if word == separator]
    for example_index, (start, end) in enumerate(zip(separator_indexes[:-1], separator_indexes[1:]), start=1):
        print('Example: {}: {}'.format(example_index, input[start + 1:end]))


if __name__ == '__main__':
    input = ['ABC', 'COMMENT', 'YES', 'YES', 'NO', '123', 'COMMENT', 'GONOW', 'MAKE', 'COMMENT', 'YES', 'COMMENT']
    filter_items_between_strings(input, 'COMMENT')
