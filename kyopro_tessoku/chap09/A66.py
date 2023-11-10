import io
import sys


def debug_input():
    _INPUT = """\
12 12
2 9 11
1 1 7
1 1 4
2 3 6
1 3 5
2 3 5
1 10 12
1 4 8
1 8 11
2 10 12
1 5 9
2 6 8
    """
    sys.stdin = io.StringIO(_INPUT)

# Union-Find 木
class unionfind:
	# n 頂点の Union-Find 木を作成
	# （ここでは頂点番号が 1-indexed になるように実装しているが、0-indexed の場合は par, size のサイズは n でよい）
	def __init__(self, n):
		self.n = n
		self.par = [ -1 ] * (n + 1) # 最初は親が無い
		self.size = [ 1 ] * (n + 1) # 最初はグループの頂点数が 1

	# 頂点 x の根を返す関数
	def root(self, x):
		# 1 個先（親）がなくなる（つまり根に到達する）まで、1 個先（親）に進み続ける
		while self.par[x] != -1:
			x = self.par[x]
		return x

	# 要素 u, v を統合する関数
	def unite(self, u, v):
		rootu = self.root(u)
		rootv = self.root(v)
		if rootu != rootv:
			# u と v が異なるグループのときのみ処理を行う
			if self.size[rootu] < self.size[rootv]:
				self.par[rootu] = rootv
				self.size[rootv] += self.size[rootu]
			else:
				self.par[rootv] = rootu
				self.size[rootu] += self.size[rootv]

	#  要素 u と v が同一のグループかどうかを返す関数
	def same(self, u, v):
		return self.root(u) == self.root(v)



# O(N)
def main():
    # 入力
    N, Q = map(int, input().split())
    queries = [ list(map(int, input().split())) for i in range(Q) ]

    # クエリの処理
    uf = unionfind(N)
    for tp, u, v in queries:
        if tp == 1:
            uf.unite(u, v)
        if tp == 2:
            if uf.same(u, v):
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    # debug_input()
    main()
