import io
import sys


def debug_input():
    _INPUT = """\
8 4
1 3 16
2 4 7
1 5 13
2 4 7
    """
    sys.stdin = io.StringIO(_INPUT)


class segtree:
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.RMQ = [0] * (2 * self.size)

    def update(self, pos, x):
        pos_suffix = pos + self.size
        self.RMQ[pos_suffix] = x
        while pos_suffix > 0:
            pos_suffix //= 2
            self.RMQ[pos_suffix] = max(
                self.RMQ[pos_suffix * 2], self.RMQ[pos_suffix * 2 + 1]
            )

    def show_max(self, L, R, a, b, u):
        if R <= a or b <= L:
            return -1000000000
        if L <= a and b <= R:
            return self.RMQ[u]

        m = (a + b) // 2
        answerl = self.show_max(L, R, a, m, u * 2)
        answerr = self.show_max(L, R, m, b, u * 2 + 1)
        return max(answerl, answerr)


# O(logN)
def main():
    N, Q = map(int, input().split())
    Z = segtree(N)

    for _ in range(Q):
        Query, L, R = map(int, input().split())
        if Query == 1:
            Z.update(L - 1, R)
        if Query == 2:
            answer = Z.show_max(L - 1, R - 1, 0, Z.size, 1)
            print(answer)


if __name__ == "__main__":
    # debug_input()
    main()
