"""
https://open.kattis.com/problems/prettygoodcuberoot
The idea is to use Newton approximation to improve x until it is good enough.

Acknowledgment:
    Done with David Brink's, https://www.linkedin.com/in/david-brink-7957854/, help.
    https://math.stackexchange.com/a/575295
    https://en.wikipedia.org/wiki/Nth_root_algorithm

python prettygoodcuberoot/pgcr.py < prettygoodcuberoot/data/sample.in
"""
import sys


def pretty_good_cuberoot(cube):
    y = int(cube)

    # first guess
    x = 10 ** (1 + len(cube) // 3)

    # derivative
    d = x ** 3 - y

    while d > 0:
        # hack: subtract 1 to make sure the sequence of x's decreases
        # otherwise x could otherwise get stuck just above the real cube root
        x = x - d // (3 * x ** 2) - 1

        d = x ** 3 - y

    if (x + 1) ** 3 - y < -d:
        print(x + 1)
    else:
        print(x)


if __name__ == "__main__":
    cubes = (cube for cube in sys.stdin.readlines())
    for cube in cubes:
        pretty_good_cuberoot(cube)
