import io
import sys


def debug_input():
    _INPUT = """\
    7
    BBRRRBB
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N)
def main():
    _ = int(input())

    last = ""
    second_last = ""

    for i_color in input():
        if i_color == last and i_color == second_last:
            print("Yes")
            exit()
        second_last = last
        last = i_color

    print("No")


if __name__ == "__main__":
    # debug_input()
    main()
