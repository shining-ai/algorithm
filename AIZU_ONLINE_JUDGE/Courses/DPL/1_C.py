import io
import sys


def debug_input():
    _INPUT = """\
4 8
4 2
5 2
2 1
8 3
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, W = map(int, input().split())
    item_list = [0] * 1001
    for _ in range(N):
        v, w = map(int, input().split())
        item_list[w] = max(item_list[w], v)

    items = []
    for item_w, item_v in enumerate(item_list):
        if item_v != 0:
            items.append([item_v, item_w])

    dp = [[-1] * (W + 1) for _ in range(len(items) + 1)]
    dp[0][0] = 0

    for i_number in range(len(items)):
        for j_kg in range(W + 1):
            if dp[i_number][j_kg] != -1:
                dp[i_number + 1][j_kg] = max(
                    dp[i_number][j_kg],
                    dp[i_number + 1][j_kg],
                )

                i = 1
                while j_kg + items[i_number][1] * i <= W:
                    dp[i_number + 1][j_kg + items[i_number][1] * i] = max(
                        dp[i_number][j_kg] + items[i_number][0] * i,
                        dp[i_number + 1][j_kg + items[i_number][1] * i],
                    )
                    i += 1

    print(max(dp[len(items)]))


if __name__ == "__main__":
    debug_input()
    main()
