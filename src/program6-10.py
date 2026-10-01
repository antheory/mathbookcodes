# プログラム6-10（初期変位を表す関数phi(x)）
xa = 0.25; h = 1.0
def u_init(x):
    if x < xa:
        return h / xa * x
    else:
        return h * (l - x) / (l - xa)
