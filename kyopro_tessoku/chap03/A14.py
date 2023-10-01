import io
import sys


def debug_input():
    _INPUT = """\
    3 50
    3 9 17
    4 7 9
    10 20 30
    1 2 3
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


# 計算量: O(N+log10^9)
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))

    AB = []
    CD = []

    for i in range(N):
        for j in range(N):
            AB.append(A[i] + B[j])
            CD.append(C[i] + D[j])

    AB.sort()
    CD.sort()

    for i_ab in AB:
        res = binary_search(len(CD) - 1, CD, K - i_ab)
        if CD[res] == K - i_ab:
            print("Yes")
            sys.exit()

    print("No")


if __name__ == "__main__":
    # debug_input()
    main()
