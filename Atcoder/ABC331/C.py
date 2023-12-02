import bisect
import io
import sys


def debug_input():
    _INPUT = """\
50
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = []

    sorted_A = sorted(A)
    sum_A = [sorted_A[0]]
    for i in range(1, N):
        sum_A.append(sum_A[i - 1] + sorted_A[i])

    for i_A in A:
        point = bisect.bisect_right(sorted_A, i_A)
        ans.append(sum_A[-1] - sum_A[point - 1])

    for i_ans in ans:
        print(i_ans, end=" ")


if __name__ == "__main__":
    # debug_input()
    main()
