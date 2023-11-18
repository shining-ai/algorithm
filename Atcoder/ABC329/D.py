import io
import sys


def debug_input():
    _INPUT = """\
9 8
8 8 2 2 8 8 2 2
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    score = [0] * (N + 1)
    max_candidate = 0

    for i in A:
        score[i] += 1
        if score[i] > score[max_candidate]:
            max_candidate = i
        elif score[i] == score[max_candidate]:
            max_candidate = min(max_candidate, i)
        else:
            pass
        print(max_candidate)


if __name__ == "__main__":
    # debug_input()
    main()
