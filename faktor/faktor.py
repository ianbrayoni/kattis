"""
https://open.kattis.com/problems/faktor

Solved ny the formula (I-1)*A + 1 where I, impact and A, articles

python faktor/faktor.py < faktor/data/faktor.dummy.1.in
"""

import sys


def determine_min_citations(articles, impact):
    return (impact - 1) * articles + 1


if __name__ == "__main__":
    articles, impact = [int(n) for n in sys.stdin.readline().split()]
    print(determine_min_citations(articles, impact))
