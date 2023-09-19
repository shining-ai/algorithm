import io
import sys


def debug_input():
    _INPUT = """\
    10
    50 150 250 350 450 550 650 750 850 950
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N!)
def main():
    N = int(input())
    A_list = list(map(int, input().split()))

    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if A_list[i] + A_list[j] + A_list[k] == 1000:
                    print("Yes")
                    exit()
    print("No")


if __name__ == "__main__":
    # debug_input()
    main()
