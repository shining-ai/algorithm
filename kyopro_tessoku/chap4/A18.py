import io
import sys


def debug_input():
    _INPUT = """\
    3 7
    2 2 3
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(NS)
def main():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    result = [[0] * (S + 1) for _ in range(N + 1)]
    result[0][0] = 1

    for i in range(1, N + 1):
        for j in range(S + 1):
            if result[i - 1][j] == 1:
                result[i][j] = 1
                if j + A[i - 1] <= S:
                    result[i][j + A[i - 1]] = 1

    if result[N][S] == 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # debug_input()
    main()
