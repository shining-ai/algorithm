import io
import sys


def debug_input():
    _INPUT = """\
26 2
ABCDEFGHIJKLMNOPQRSTUVWXYZ
FG
    """

    sys.stdin = io.StringIO(_INPUT)


##NGのコード
def main():
    N, M = map(int, input().split())
    S = input()
    T = input()

    max_pos = 0
    min_pos = N

    ans = "No"
    for i in range(N - M + 1):
        if S[i : i + M] == T:
            ans = "Yes"
            max_pos = max(max_pos, i)
            min_pos = min(min_pos, i)

    if min_pos != 0 and ans == "Yes":
        for i in range(min_pos):
            if S[i] == S[i + 1]:
                if S[i] != T[0]:
                    ans = "No"
                    break

    if max_pos != N - M and ans == "Yes":
        for i in range(N - M + 1, max_pos + M, -1):
            if S[i] == S[i - 1]:
                if S[i] != T[-1]:
                    ans = "No"
                    break

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
