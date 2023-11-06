import io
import sys
from collections import deque


def debug_input():
    _INPUT = """\
6 6
1 4
2 3
3 4
5 6
1 2
2 4
    """
    sys.stdin = io.StringIO(_INPUT)


# O(N)
def main():
    N, M = map(int, input().split())
    res = [list() for _ in range(N + 1)]

    for _ in range(M):
        A, B = map(int, input().split())
        res[A].append(B)
        res[B].append(A)

    dist = [-1] * (N + 1)
    dist[1] = 0
    Q = deque()
    Q.append(1)

    while len(Q) > 0:
        pos = Q.popleft()
        for i in res[pos]:
            if dist[i] == -1:
                dist[i] = dist[pos] + 1
                Q.append(i)

    for i in range(1, N + 1):
        print(dist[i])


if __name__ == "__main__":
    # debug_input()
    main()
