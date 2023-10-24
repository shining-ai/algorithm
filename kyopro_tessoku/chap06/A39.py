import io
import sys


def debug_input():
    _INPUT = """\
    3
    123 86399
    1 86400
    86399 86400
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N*logN)
def main():
    N = int(input())

    schedule = []
    current_time = 0
    result = 0

    for _ in range(N):
        schedule.append(list(map(int, input().split())))

    schedule.sort(key=lambda x: x[1])

    for i in range(N):
        if current_time <= schedule[i][0]:
            current_time = schedule[i][1]
            result += 1

    print(result)


if __name__ == "__main__":
    # debug_input()
    main()
