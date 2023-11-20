import io
import sys


def debug_input():
    _INPUT = """\
competitive
programming

    """

    sys.stdin = io.StringIO(_INPUT)


# 編集距離（レーベンシュタイン距離）
# 計算量: O(ST)
def main():
    S = input()
    T = input()

    s_num = len(S)
    t_num = len(T)

    dp = [[None] * (t_num + 1) for i in range(s_num + 1)]
    for i in range(s_num + 1):
        dp[i][0] = i
    for i in range(t_num + 1):
        dp[0][i] = i

    for i_s in range(1, s_num + 1):
        for j_t in range(1, t_num + 1):
            if S[i_s - 1] == T[j_t - 1]:
                dp[i_s][j_t] = min(
                    dp[i_s - 1][j_t] + 1,
                    dp[i_s][j_t - 1] + 1,
                    dp[i_s - 1][j_t - 1],
                )
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
