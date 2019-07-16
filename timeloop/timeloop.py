"""
https://open.kattis.com/problems/timeloop

Print `num Abracadabra` N times

python timeloop/timeloop.py < timeloop/data/a.in
"""
import sys

if __name__ == "__main__":
    count = int(sys.stdin.readline())

    for i in range(1, count + 1):
        print(i, "Abracadabra")
