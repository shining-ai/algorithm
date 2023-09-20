import io
import sys


def debug_input():
    _INPUT = """\
    3 6
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N^2)
def main():
    N, K = map(int, input().split())
    result = 0

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if 1 <= K - i - j <= N:
                result += 1

    print(result)


if __name__ == "__main__":
    # debug_input()
    main()
