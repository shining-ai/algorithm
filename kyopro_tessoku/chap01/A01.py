import io
import sys

_INPUT = """\
2
"""

sys.stdin = io.StringIO(_INPUT)

# 計算量: O(1)
if __name__ == "__main__":
    input_n = int(input())
    print(input_n**2)
