import io
import sys


def debug_input():
    _INPUT = """\
    13
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(10+10)
def main():
    N = int(input())

    result = [0] * 10
    bit = 0
    base = 512
    while base > 1:
        if N / base >= 1:
            result[bit] = 1
            N -= base
        base /= 2
        bit += 1

    if N == 1:
        result[9] = 1

    for i_ans in result:
        print(i_ans, end="")
    print()


if __name__ == "__main__":
    # debug_input()
    main()
