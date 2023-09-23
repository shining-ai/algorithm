import io
import sys


def debug_input():
    _INPUT = """\
    7
    0 1 1 0 1 0 0
    3
    2 5
    2 7
    5 7
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N + Q)
def main():
    _ = int(input())
    A = list(map(int, input().split()))
    prefix_sum_win = [0]
    prefix_sum_lose = [0]

    for i_a in A:
        if i_a:
            prefix_sum_win.append(prefix_sum_win[-1] + 1)
            prefix_sum_lose.append(prefix_sum_lose[-1])
        else:
            prefix_sum_win.append(prefix_sum_win[-1])
            prefix_sum_lose.append(prefix_sum_lose[-1] + 1)

    Q = int(input())
    for i_q in range(Q):
        start_num, end_num = map(int, input().split())
        win = prefix_sum_win[end_num] - prefix_sum_win[start_num - 1]
        lose = prefix_sum_lose[end_num] - prefix_sum_lose[start_num - 1]
        if win > lose:
            print("win")
        elif win < lose:
            print("lose")
        else:
            print("draw")


if __name__ == "__main__":
    # debug_input()
    main()
