import heapq
import io
import sys


def debug_input():
    _INPUT = """\
    3
    1 2420
    1 1650
    2
    """
    sys.stdin = io.StringIO(_INPUT)


def main():
    Q = int(input())
    h = []

    for _ in range(Q):
        query = list(input().split())
        if query[0] == "1":
            heapq.heappush(h, int(query[1]))
        elif query[0] == "2":
            print(h[0])
        else:
            heapq.heappop(h)


if __name__ == "__main__":
    # debug_input()
    main()
