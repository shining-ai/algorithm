import io
import sys


def debug_input():
    _INPUT = """\
12
ssskkyskkkky
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    S = input()

    num = [0] * 26
    pre_s = 0
    s_num = 0

    for s in S:
        if ord(s) - ord("a") == pre_s:
            s_num += 1
        else:
            s_num = 1

        if num[ord(s) - ord("a")] < s_num:
            num[ord(s) - ord("a")] = s_num

        pre_s = ord(s) - ord("a")

    print(sum(num))


if __name__ == "__main__":
    # debug_input()
    main()
