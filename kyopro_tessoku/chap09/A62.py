import io
import sys


def debug_input():
    _INPUT = """\
3 2
1 3
2 3
    """
    sys.stdin = io.StringIO(_INPUT)


def dfs(pos, G, visited):
    visited[pos] = True
    for i in G[pos]:
        if visited[i] == False:
            dfs(i, G, visited)


# O(N)
def main():
    N, M = map(int, input().split())
    res = [list() for _ in range(N + 1)]

    for _ in range(M):
        A, B = map(int, input().split())
        res[A].append(B)
        res[B].append(A)

    visited = [False] * (N + 1)
    dfs(1, res, visited)

    answer = True
    for i in range(1, N + 1):
        if visited[i] == False:
            answer = False

    if answer:
        print("The graph is connected.")
    else:
        print("The graph is not connected.")


if __name__ == "__main__":
    # debug_input()
    main()
