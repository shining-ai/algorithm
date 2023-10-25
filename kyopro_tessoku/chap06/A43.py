import io
import sys


def debug_input():
    _INPUT = """\
    3 100
    20 E
    50 E
    70 W
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N)
def main():
    N, L = map(int, input().split())
    ans = 0

    for _ in range(N):
        A, B = input().split()
        if B == "E":
            time = L - int(A)
        else:
            time = int(A)
        ans = max(ans, time)

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
