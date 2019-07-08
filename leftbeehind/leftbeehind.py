"""
https://open.kattis.com/problems/leftbeehind

python leftbeehind/leftbeehind.py < leftbeehind/data/test0.in
"""

import sys


def leftbeehind(jar):
    sweet_jar = int(jar[0])
    sour_jar = int(jar[1])

    superstitious_number = 13

    if (sweet_jar + sour_jar) == superstitious_number:
        return "Never speak again."

    if sweet_jar > sour_jar:
        return "To the convention."
    elif sweet_jar < sour_jar:
        return "Left beehind."
    else:
        return "Undecided."


if __name__ == "__main__":
    # ignore last element - Input is terminated by a line containing two zeros,
    # which should not be processed.
    jars = (n.split() for n in sys.stdin.readlines()[:-1])
    for jar in jars:
        print(leftbeehind(jar))

