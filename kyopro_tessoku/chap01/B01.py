import io
import sys

_INPUT = """\
1 2
"""

sys.stdin = io.StringIO(_INPUT)

# 計算量: O(1)
if __name__ == "__main__":
    input_a, input_b = map(int, input().split())
    print(input_a + input_b)
