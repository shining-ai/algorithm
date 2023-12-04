import io
import sys


def debug_input():
    _INPUT = """\
8 2000000000
735206213 589759002
69834511 668882481
808284659 201886572
14983332 86000815
361784848 761170565
801013198 730103626
5748439 576460932
267998019 287998488
    """

    sys.stdin = io.StringIO(_INPUT)


def make_item_list(item_list, item_num):
    # それぞれ、「品物を選ばなかった場合」、「品物を一つ選んだ場合」、・・・、「品物を全部選んだ場合」の組み合わせに対応する[価値,重さ]をリスト化していく
    for _ in range(item_num):
        v, w = map(int, input().split())
        for i in range(len(item_list)):
            bag = [
                item_list[i][0] + v,
                item_list[i][1] + w,
            ]
            item_list.append(bag)

    return item_list


def main():
    N, W = map(int, input().split())

    # 半分全列挙で解く
    first_half = N // 2
    second_half = N - first_half

    # それぞれ[価値,重さ]を入れるリストを作る
    first_list = [[0, 0]]
    second_list = [[0, 0]]

    first_list = make_item_list(first_list, first_half)
    second_list = make_item_list(second_list, second_half)

    # 重さでソート
    first_list.sort(key=lambda x: x[1])
    second_list.sort(key=lambda x: x[1])

    # 重さがWを超えるものを除外
    first_list = [x for x in first_list if x[1] <= W]
    second_list = [x for x in second_list if x[1] <= W]

    # 価値が大きいものを残す
    for i in range(len(first_list) - 1):
        if first_list[i + 1][0] < first_list[i][0]:
            first_list[i + 1][0] = first_list[i][0]

    for i in range(len(second_list) - 1):
        if second_list[i + 1][0] < second_list[i][0]:
            second_list[i + 1][0] = second_list[i][0]

    ans = 0
    i = 0
    j = len(second_list) - 1
    while i < len(first_list) and j >= 0:
        if first_list[i][1] + second_list[j][1] <= W:
            ans = max(ans, first_list[i][0] + second_list[j][0])
            i += 1
        else:
            j -= 1

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
