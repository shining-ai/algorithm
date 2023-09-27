import copy

# import io
# import sys


# def debug_input():
#     _INPUT = """\
#     7
#     1 2 5 5 2 3 1
#     2
#     3 5
#     4 6
#     """

#     sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N+D)
def main():
    N = int(input())
    A = list(map(int, input().split()))
    D = int(input())

    A_max_left = copy.deepcopy(A)
    A_max_right = copy.deepcopy(A)

    for i_left in range(1, N):
        A_max_left[i_left] = max(A_max_left[i_left - 1], A_max_left[i_left])

    for i_right in range(N - 2, -1, -1):
        A_max_right[i_right] = max(
            A_max_right[i_right + 1], A_max_right[i_right]
        )

    for _ in range(D):
        L, R = map(int, input().split())
        print(max(A_max_left[L - 2], A_max_right[R]))


if __name__ == "__main__":
    # debug_input()
    main()
