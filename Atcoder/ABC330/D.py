import io
import sys


def debug_input():
    _INPUT = """\
15
xooxxooooxxxoox
oxxoxoxxxoxoxxo
oxxoxoxxxoxoxxx
ooooxooooxxoxxx
oxxoxoxxxoxoxxx
oxxoxoxxxoxoxxo
oxxoxooooxxxoox
xxxxxxxxxxxxxxx
xooxxxooxxxooox
oxxoxoxxoxoxxxo
xxxoxxxxoxoxxoo
xooxxxooxxoxoxo
xxxoxxxxoxooxxo
oxxoxoxxoxoxxxo
xooxxxooxxxooox

    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(2N)
def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    count_row = []
    count_col = []

    for i in range(N):
        count_row.append(S[i].count("o"))

    for i in range(N):
        num = 0
        for j in range(N):
            if S[j][i] == "o":
                num += 1
        count_col.append(num)

    ans = 0
    for i in range(N):
        for j in range(N):
            if S[i][j] == "o":
                ans += (count_row[i] - 1) * (count_col[j] - 1)

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
