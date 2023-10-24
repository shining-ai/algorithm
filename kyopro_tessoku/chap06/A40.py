import io
import sys


def debug_input():
    _INPUT = """\
    7
    1 2 1 2 1 2 1
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N)
def main():
    _ = int(input())

    bar_num = [0] * 101
    result = 0

    for i in map(int, input().split()):
        bar_num[i] += 1

    for i_bar in bar_num:
        if i_bar >= 3:
            result += i_bar * (i_bar - 1) * (i_bar - 2) // 6

    print(result)


if __name__ == "__main__":
    # debug_input()
    main()
