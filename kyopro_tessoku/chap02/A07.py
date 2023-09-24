import io
import sys


def debug_input():
    _INPUT = """\
    3
    2
    1 3
    2 3
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N + D)
def main():
    D = int(input())
    N = int(input())
    attendees = [0] * (D + 2)

    for _ in range(N):
        start_day, end_day = map(int, input().split())
        attendees[start_day] += 1
        attendees[end_day + 1] -= 1

    for i_d in range(1, D + 1):
        attendees[i_d] += attendees[i_d - 1]

    attendees.pop(0)
    attendees.pop(-1)
    for i_attendee in attendees:
        print(i_attendee)


if __name__ == "__main__":
    # debug_input()
    main()
