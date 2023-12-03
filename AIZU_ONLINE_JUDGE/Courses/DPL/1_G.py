import io
import sys


def debug_input():
    _INPUT = """\
2 100
1 1 100
2 1 50
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, W = map(int, input().split())

    # アイテムを複数個単位(2進数)で分割して考える
    item_list = [(0, 0)]
    for i_item in range(N):
        v, w, m = map(int, input().split())
        x = 1
        while m > 0:
            if m < x:
                x = 1
            item_list.append((v * x, w * x))
            m -= x
            x *= 2

    dp = [[-1] * ((W + 1)) for _ in range(len(item_list) + 1)]
    dp[0][0] = 0

    for i_item in range(1, len(item_list) + 1):
        for i_kg in range(W + 1):
            if dp[i_item - 1][i_kg] != -1:
                dp[i_item][i_kg] = max(
                    dp[i_item - 1][i_kg],
                    dp[i_item][i_kg],
                )
                item_kg = item_list[i_item - 1][1]
                if i_kg + item_kg <= W:
                    dp[i_item][i_kg + item_kg] = max(
                        dp[i_item - 1][i_kg] + item_list[i_item - 1][0],
                        dp[i_item][i_kg + item_kg],
                    )

    print(max(dp[-1]))


if __name__ == "__main__":
    # debug_input()
    main()
