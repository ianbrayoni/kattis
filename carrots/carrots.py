"""
https://open.kattis.com/problems/carrots

All that was needed is to output P, the number of problems solved

python carrots/carrots.py < carrots/data/carrots.01.in
"""
import sys

if __name__ == "__main__":
    _, problems_solved = sys.stdin.readline().split()
    print(problems_solved)
