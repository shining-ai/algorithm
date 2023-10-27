import io
import sys
from collections import deque


def debug_input():
    _INPUT = """\
    5
    1 taro
    1 hanako
    2
    3
    2
    """
    sys.stdin = io.StringIO(_INPUT)


def main():
    Q = int(input())
    S = deque()

    for _ in range(Q):
        query = list(input().split())
        if query[0] == "1":
            S.append(query[1])
        elif query[0] == "2":
            print(S[0])
        else:
            S.popleft()


if __name__ == "__main__":
    # debug_input()
    main()
