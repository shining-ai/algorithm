import io
import sys


def debug_input():
    _INPUT = """\
    4 7
    3 13
    3 17
    5 29
    1 10
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(NS)
def main():
    N, W = map(int, input().split())

    result = [[-1] * (W + 1) for _ in range(N + 1)]
    result[0][0] = 0
    ans = 0

    for i_item in range(1, N + 1):
        w, v = map(int, input().split())
        for j_kg in range(W + 1):
            if result[i_item - 1][j_kg] >= 0:
                result[i_item][j_kg] = max(
                    result[i_item - 1][j_kg], result[i_item][j_kg]
                )
                if j_kg + w <= W:
                    result[i_item][j_kg + w] = max(
                        result[i_item - 1][j_kg] + v, result[i_item][j_kg + w]
                    )

                    ans = max(ans, result[i_item][j_kg + w])

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
