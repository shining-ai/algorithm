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


def update(RMQ, pos, x, size):
    RMQ[pos + size] = x
    while pos > 0:
        RMQ[pos] = max(RMQ[pos * 2], RMQ[pos * 2 + 1])
        pos //= 2

    return RMQ


def show_max(RMQ, L, R, a, b, u):
    if R <= a or b <= 1:
        return -1000000000
    if L <= a and b <= R:
        return RMQ[u]

    m = (a + b) // 2
    answerl = show_max(RMQ, L, R, a, m, u * 2)
    answerr = show_max(RMQ, L, R, m, b, u * 2 + 1)
    return max(answerl, answerr)


# O
def main():
    N, Q = map(int, input().split())

    size = 1
    while size < N:
        size *= 2
    RMQ = [0] * (2 * size)

    for _ in range(Q):
        Query, L, R = map(int, input().split())
        if Query == 1:
            RMQ = update(RMQ, L, R, size)
        elif Query == 2:
            answer = show_max(RMQ, L - 1, R - 1, 0, size, 1)
            print(answer)


if __name__ == "__main__":
    debug_input()
    main()
