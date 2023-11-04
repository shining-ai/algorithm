import io
import sys
from collections import deque


def debug_input():
    _INPUT = """\
6
6 2 5 3 1 4
    """
    sys.stdin = io.StringIO(_INPUT)


# O(logN)
def main():
    N = int(input())
    A = list(map(int, input().split()))

    answer = [None] * N
    level2 = deque()
    for i in range(N):
        if i >= 1:
            level2.append((i, A[i - 1]))
            while len(level2) >= 1:
                kabuka = level2[-1][1]  # 株価はタプルの 2 番目の要素
                if kabuka <= A[i]:
                    level2.pop()
                else:
                    break
        if len(level2) >= 1:
            answer[i] = level2[-1][0]  # 日付はタプルの 1 番目の要素
        else:
            answer[i] = -1

    # answer を空白区切りで出力
    print(*answer)


if __name__ == "__main__":
    # debug_input()
    main()
