"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""


def count_th(word):
    # TBC
    substr = "th"

    if len(word) < 2:
        return 0
    if substr == word[:2]:
        # print(word[:2])
        return count_th(word[1:]) + 1
    else:
        return count_th(word[1:])

    # pass


print(count_th("abcthfgth"))
