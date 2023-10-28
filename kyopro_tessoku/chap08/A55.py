import bisect
import io
import sys


def debug_input():
    _INPUT = """\
    3
    1 77
    3 40
    3 80
    """
    sys.stdin = io.StringIO(_INPUT)


# 集合
# set型を使うとtimeoutなので、listで実装する
def main():
    Q = int(input())
    desk = []

    for _ in range(Q):
        query = list(input().split())
        if query[0] == "1":
            if desk == []:
                desk.append(int(query[1]))
                continue
            pos = bisect.bisect_left(desk, int(query[1]))
            desk.insert(pos, int(query[1]))
        elif query[0] == "2":
            desk.pop(bisect.bisect_left(desk, int(query[1])))
        else:
            if desk == []:
                print(-1)
                continue
            if desk[-1] < int(query[1]):
                print(-1)
            else:
                print(desk[bisect.bisect_left(desk, int(query[1]))])


if __name__ == "__main__":
    # debug_input()
    main()
