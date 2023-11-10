import io
import sys


def debug_input():
    _INPUT = """\
7
1 1 3 2 4 4
    """
    sys.stdin = io.StringIO(_INPUT)


# O(N)
def main():
    N = int(input())
    A = list(map(int, input().split()))
    res = [0] * (N + 1)

    for i, boss in enumerate(reversed(A)):
        res[boss] += 1 + res[N - i]

    res.pop(0)
    for i in res:
        print(i, end=" ")
    print()


if __name__ == "__main__":
    # debug_input()
    main()
