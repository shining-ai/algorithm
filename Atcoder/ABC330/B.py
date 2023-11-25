import io
import sys


def debug_input():
    _INPUT = """\
3 10 10
11 10 9

    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(2N)
def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))

    ans = []
    for i_a in A:
        if L <= i_a <= R:
            ans.append(i_a)
        else:
            if i_a < L:
                ans.append(L)
            else:
                ans.append(R)

    ans = " ".join(map(str, ans))
    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
