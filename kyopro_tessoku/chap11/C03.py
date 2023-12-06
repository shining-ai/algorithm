import io
import sys


def debug_input():
    _INPUT = """\
5
30
-10
20
-10
20
3
1 2
3 5
1 4
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    D = int(input())
    A = [int(input())]
    for _ in range(D - 1):
        A.append(int(input()) + A[-1])

    Q = int(input())
    for _ in range(Q):
        S, T = map(int, input().split())

        if A[S - 1] > A[T - 1]:
            print(S)
        elif A[S - 1] < A[T - 1]:
            print(T)
        else:
            print("Same")


if __name__ == "__main__":
    # debug_input()
    main()
