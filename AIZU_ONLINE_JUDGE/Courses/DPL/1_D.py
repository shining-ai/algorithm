import io
import sys
import bisect


def debug_input():
    _INPUT = """\
2
0
0
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    dp = [0] * (N + 1)
    L = [-1]
    ans = 0
    for i in range(1, N + 1):
        a = int(input())
        combo = bisect.bisect_left(L, a)
        dp[i] = combo

        if ans < combo:
            L.append(a)
            ans = combo
        else:
            L[combo] = min(L[combo], a)
    
    print(ans)


if __name__ == "__main__":
    debug_input()
    main()
