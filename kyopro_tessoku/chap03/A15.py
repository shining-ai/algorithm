import io
import sys


def debug_input():
    _INPUT = """\
    5
    46 80 11 77 46
    """

    sys.stdin = io.StringIO(_INPUT)


def binary_search(N, A, X):
    L = 0
    R = N
    while L < R:
        mid = (L + R) // 2
        if A[mid] < X:
            L = mid + 1
        else:
            R = mid

    return L


# 計算量: O(NlogN)
def main():
    N = int(input())
    A = list(map(int, input().split()))
    T = list(set(A))

    T.sort()

    for i in range(N):
        print(binary_search(len(T), T, A[i]) + 1, end=" ")

    print()


if __name__ == "__main__":
    # debug_input()
    main()
