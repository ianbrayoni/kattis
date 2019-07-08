"""
https://open.kattis.com/problems/elevatortrouble
https://www.khanacademy.org/computing/computer-science/algorithms/breadth-first-search/a/the-breadth-first-search-algorithm

python elevatortrouble/elevatortrouble.py < elevatortrouble/data/1.in
"""
import sys
from collections import deque


class Node:
    """
    class object to hold current floor position and steps required to get to it
    """

    def __init__(self, floor, step):
        self.floor = floor
        self.step = step


def find_pushes(data):
    data = [int(x) for x in data]
    floors, start, goal, up, down = data

    queue = deque()
    queue.append(Node(start, 0))

    visited = [False for x in range(floors + 1)]
    visited[start] = True

    pushes = -1

    if start == goal:
        print(0)
        return

    while len(queue):
        current = queue.popleft()

        if (current.floor + up) <= floors and not visited[current.floor + up]:
            if (current.floor + up) == goal:
                pushes = current.step + 1
                break
            else:
                visited[current.floor + up] = True
                queue.append(Node(current.floor + up, current.step + 1))

        if (current.floor - down) >= 1 and not visited[current.floor - down]:
            if (current.floor - down) == goal:
                pushes = current.step + 1
                break
            else:
                visited[current.floor - down] = True
                queue.append(Node(current.floor - down, current.step + 1))

    if pushes == -1:
        print("use the stairs")
    else:
        print(pushes)


if __name__ == "__main__":
    data = sys.stdin.readline().split()
    find_pushes(data)
