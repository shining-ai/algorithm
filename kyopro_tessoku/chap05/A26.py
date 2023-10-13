import io
import sys


def debug_input():
    _INPUT = """\
    4
    17
    31
    35
    49
    """

    sys.stdin = io.StringIO(_INPUT)


def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False

        i += 1

    return True


# 計算量: O(2N)
def main():
    Q = int(input())

    for i in range(Q):
        X = int(input())
        if is_prime(X):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    # debug_input()
    main()
