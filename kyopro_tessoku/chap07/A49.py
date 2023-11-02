import io
import sys


def debug_input():
    _INPUT = """\
    3
    1 2 3
    2 3 4
    3 4 5
    """
    sys.stdin = io.StringIO(_INPUT)


def calc_plus_score(field, P, Q, R):
    field[P - 1] += 1
    field[Q - 1] += 1
    field[R - 1] += 1

    return field.count(0)


def calc_minus_score(field, P, Q, R):
    field[P - 1] -= 1
    field[Q - 1] -= 1
    field[R - 1] -= 1

    return field.count(0)


def calc_score(field, P, Q, R):
    plus_score = calc_plus_score(field, P, Q, R)
    minux_score = calc_minus_score(field, P, Q, R)

    return plus_score, minux_score


# ビームサーチ
def main():
    T = int(input())
    score = 0
    field = [0] * 20

    P, Q, R = map(int, input().split())
    temp_A, temp_B = calc_score(field, P, Q, R)

    P_next, Q_next, R_next = map(int, input().split())
    next_score = [
        temp_A + calc_plus_score(field, P_next, Q_next, R_next),
        temp_A + calc_minus_score(field, P_next, Q_next, R_next),
        temp_B + calc_plus_score(field, P_next, Q_next, R_next),
        temp_B + calc_minus_score(field, P_next, Q_next, R_next),
    ]
    if next_score.index(max(next_score)) <= 1:
        print("A")
    else:
        print("B")

    # P_pre, Q_pre, R_pre = map(int, input().split())

    # next_score1 = 0


if __name__ == "__main__":
    debug_input()
    main()
