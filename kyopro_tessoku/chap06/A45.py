import io
import sys


def debug_input():
    _INPUT = """\
    4 B
WBBR
    """

    sys.stdin = io.StringIO(_INPUT)


def print_res(val, C_VAL):
    if val % 3 == C_VAL:
        print("Yes")
    else:
        print("No")


# 計算量: O(N)
def main():
    N, C = input().split()
    A = input()

    W_VAL = 0
    B_VAL = 1
    R_VAL = 2

    val = 0

    for i_a in A:
        if i_a == "R":
            val += R_VAL
        elif i_a == "W":
            val += W_VAL
        elif i_a == "B":
            val += B_VAL

    if C == "R":
        print_res(val, R_VAL)
    elif C == "W":
        print_res(val, W_VAL)
    elif C == "B":
        print_res(val, B_VAL)


if __name__ == "__main__":
    # debug_input()
    main()
