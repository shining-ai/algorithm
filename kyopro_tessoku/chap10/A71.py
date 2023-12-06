import io
import sys


def debug_input():
    _INPUT = """\
3
10 20 30
35 40 33
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort(reverse=True)

    ans = 0
    for i in range(N):
        ans += A[i] * B[i]

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
