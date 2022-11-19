#!/usr/bin/python3
"""Python interpreter"""


def text_indentation(text):
    """prints a text with 2 new lines
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    specialChar = False
    begins = 0
    for idx in range(len(text)):
        if text[idx] in ".:?":
            specialChar = True
            ends = idx + 1
            print(text[begins:ends].lstrip(), end='\n\n')
            begins = ends
        if specialChar is True and idx == len(text) - 1:
            print(text[begins:].lstrip(), end='')

    if specialChar is False:
        print(text.lstrip(), end="")
