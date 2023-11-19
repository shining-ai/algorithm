import io
import sys


def debug_input():
    _INPUT = """\
30
<<><>>><><>><><><<>><<<><><<>
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    S = input()

    combo = 0
    ans = 0

    for i_s in range(N - 1):
        if S[i_s] == ">":
            combo += 1
        else:
            ans += (1 + combo) * combo // 2
            combo = 0

    ans += (1 + combo) * combo // 2

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
