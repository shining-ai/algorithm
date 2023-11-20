import io
import sys


def debug_input():
    _INPUT = """\
tokyo
kyoto
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(ST)
def main():
    S = " " + input()
    T = " " + input()

    s_num = len(S)
    t_num = len(T)

    dp = [[0] * (t_num) for _ in range(s_num)]

    for i_s in range(1, s_num):
        for j_t in range(1, t_num):
            if S[i_s] == T[j_t]:
                dp[i_s][j_t] = max(
                    dp[i_s - 1][j_t],
                    dp[i_s][j_t - 1],
                    dp[i_s - 1][j_t - 1] + 1,
                )
            else:
                dp[i_s][j_t] = max(
                    dp[i_s - 1][j_t],
                    dp[i_s][j_t - 1],
                )

    print(dp[-1][-1])


if __name__ == "__main__":
    # debug_input()
    main()
