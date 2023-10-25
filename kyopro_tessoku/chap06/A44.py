import io
import sys


def debug_input():
    _INPUT = """\
    5 4
    1 4 8
    3 2
    2
    3 2
    """

    sys.stdin = io.StringIO(_INPUT)


def Query1(flag_rev, A, x, y, N):
    if flag_rev:
        A[-x] = y
    else:
        A[x - 1] = y

    return A


def Query3(flag_rev, A, x, N):
    if flag_rev:
        print(A[-x])
    else:
        print(A[x - 1])

    return A


# 計算量: O(N)
def main():
    N, Q = map(int, input().split())
    A = list(i for i in range(1, N + 1))
    flag_rev = False

    for _ in range(Q):
        Query = list(map(int, input().split()))
        if Query[0] == 1:
            Query1(flag_rev, A, Query[1], Query[2], N)
        elif Query[0] == 2:
            flag_rev = not flag_rev
        else:
            Query3(flag_rev, A, Query[1], N)


if __name__ == "__main__":
    # debug_input()
    main()
