import io
import sys


def debug_input():
    _INPUT = """\
    7
    1 1
    4 1
    2 5
    3 4
    3 2
    4 2
    5 5
    """
    sys.stdin = io.StringIO(_INPUT)


def dist(pos1, pos2):
    return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** (1 / 2)


# 貪欲法
def main():
    N = int(input())
    city_list = []
    start = 0

    for i in range(N):
        pos = list(map(int, input().split()))
        pos.append(i + 1)
        city_list.append(pos)

    current_pos = city_list.pop(start)
    start = current_pos[-1]
    print(start)

    for _ in range(N - 1):
        dist_list = []
        for pos in city_list:
            dist_list.append(dist(current_pos, pos))
        current = dist_list.index(min(dist_list))
        current_pos = city_list.pop(current)
        print(current_pos[-1])

    print(start)


if __name__ == "__main__":
    # debug_input()
    main()
