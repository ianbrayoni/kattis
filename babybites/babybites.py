"""
https://open.kattis.com/problems/babybites
python babybites/babybites.py < babybites/data/3.in
"""

import sys


def validate_count(no_bites, spoken_words):

    validator = (x + 1 for x in range(no_bites))
    result = zip(validator, spoken_words)

    for count in result:
        if count[1] != "mumble" and count[0] != int(count[1]):
            return "something is fishy"

    return "makes sense"


if __name__ == "__main__":
    no_bites = int(sys.stdin.readline())
    spoken_words = sys.stdin.readline().rstrip().split(" ")

    print(validate_count(no_bites, spoken_words))
