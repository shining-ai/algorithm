import io
import sys


def debug_input():
    _INPUT = """\
    3
    1 tanaka 49
    1 suzuki 50
    2 tanaka
    """
    sys.stdin = io.StringIO(_INPUT)

# 連想配列(辞書型)
def main():
    Q = int(input())
    score = {}

    for _ in range(Q):
        query = list(input().split())
        if query[0] == "1":
            score[query[1]] = int(query[2])
        elif query[0] == "2":
            print(score[query[1]])


if __name__ == "__main__":
    # debug_input()
    main()
