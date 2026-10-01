# プログラム6-4（初期条件1: phi1(x)）
xa = 0.25 * l; u0 = 1.0   #   a = l / 4 の場合
def u_init(x):
    if x < xa:
        return 0
    elif x < (l-xa):
        return u0
    else:
        return 0
