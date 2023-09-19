import io
import sys

_INPUT = """\
5 40
10 20 30 40 50
"""

sys.stdin = io.StringIO(_INPUT)

# 計算量: O(N)
if __name__ == "__main__":
    N, X = map(int, input().split())
    A_list = list(map(int, input().split()))

    for i_A in A_list:
        if i_A == X:
            print("Yes")
            exit()
    print("No")
