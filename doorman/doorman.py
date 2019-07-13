"""
https://open.kattis.com/problems/doorman

python doorman/doorman.py < doorman/data/doorman.1.in
"""

import sys
from collections import deque


def max_revellers(diff, genders):
    diff = int(diff)
    temp_diff = 0
    q = deque()

    if diff == 0:
        return len(genders)

    # simulate a queue
    for gender in genders:
        q.append(gender)

    men = 0
    women = 0
    q_len = len(q)

    # we shall use FIFO unless where we can admit next in line
    while q_len > 1 and temp_diff <= diff:
        current = q[0]
        next_in_line = q[1]

        # if there's more men than women, admit a woman
        if (men - women) >= diff and next_in_line == "W":
            women += 1

            if current == "W":
                q.popleft()
            else:
                del q[1]

        # if there's more women than men, admit a man
        elif (women - men) >= diff and next_in_line == "M":
            men += 1
            if current == "M":
                q.popleft()
            else:
                del q[1]

        # if men == women, just admit first in line
        else:
            if current == "M":
                q.popleft()
                men += 1
            else:
                q.popleft()
                women += 1

        temp_diff = abs(women - men)

        q_len -= 1

    if q_len == 1:
        # we are at the end of the queue, diff is ok - admit last guy
        count = men + women + 1
    else:
        # remove guy that messes up diff
        count = men + women - 1

    return count


if __name__ == "__main__":
    diff, genders = [input.rstrip() for input in sys.stdin.readlines()]
    print(max_revellers(diff, genders))
