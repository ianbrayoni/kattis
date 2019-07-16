"""
https://open.kattis.com/problems/judgingmoose

if-checks to determine how many points a moose has.

python judgingmoose/judgingmoose.py < judgingmoose/data/1.in
"""
import sys


def pointed_moose(left, right):
    if left == 0 and right == 0:
        verdict = "Not a moose"
    elif left == right:
        verdict = f"Even {left + right}"
    elif left > right:
        verdict = f"Odd {left * 2}"
    elif right > left:
        verdict = f"Odd {right * 2}"

    return verdict


if __name__ == "__main__":
    left, right = [int(n) for n in sys.stdin.readline().split()]
    print(pointed_moose(left, right))
