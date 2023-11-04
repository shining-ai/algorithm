import io
import sys


def debug_input():
    _INPUT = """\
5 4
1 2
2 3
3 4
1 4
    """
    sys.stdin = io.StringIO(_INPUT)


# O(N)
def main():
    N, M = map(int, input().split())
    res = [set() for _ in range(N + 1)]

    for _ in range(M):
        A, B = map(int, input().split())
        res[A].add(B)
        res[B].add(A)

    for i in range(1, N + 1):
        if len(res[i]) != 0:
            print(f"{i}: {res[i]}")
        else:
            print(str(i) + ": {}")


if __name__ == "__main__":
    # debug_input()
    main()
