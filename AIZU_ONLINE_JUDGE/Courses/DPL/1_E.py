import bisect
import io
import sys


def debug_input():
    _INPUT = """\
aizuzia
aizudai
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    S = " " + input()
    T = " " + input()

    s_num = len(S)
    t_num = len(T)

    dp = [[0] * (t_num) for _ in range(s_num)]

    for i in range(1, s_num):
        dp[i][0] = i
    for i in range(1, t_num):
        dp[0][i] = i

    for i_s in range(1, s_num):
        for j_t in range(1, t_num):
            if S[i_s] == T[j_t]:
                dp[i_s][j_t] = dp[i_s - 1][j_t - 1]
            else:
                dp[i_s][j_t] = min(
                    dp[i_s - 1][j_t] + 1,
                    dp[i_s][j_t - 1] + 1,
                    dp[i_s - 1][j_t - 1] + 1,
                )

    print(dp[-1][-1])


if __name__ == "__main__":
    # debug_input()
    main()
