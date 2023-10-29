import io
import sys


def debug_input():
    _INPUT = """\
    7 3
abcbabc
    1 3 5 7
    1 5 2 6
    1 2 6 7
    """
    sys.stdin = io.StringIO(_INPUT)


# hash値を使った比較
def main():
    N, Q = map(int, input().split())
    S = input()

    S_ascii = list(map(lambda c: ord(c), S))

    MOD = 2147483647
    power100 = [None] * (N + 1)
    power100[0] = 1
    for i in range(N):
        power100[i + 1] = power100[i] * 100 % MOD

    hash = [None] * (N + 1)
    hash[0] = 0
    for i in range(N):
        hash[i + 1] = (hash[i] * 100 + S_ascii[i]) % MOD

    def hash_value(l, r):
        return (hash[r] - hash[l - 1] * power100[r - l + 1]) % MOD

    for _ in range(Q):
        a, b, c, d = map(int, input().split())
        hash1 = hash_value(a, b)
        hash2 = hash_value(c, d)
        if hash1 == hash2:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    # debug_input()
    main()
