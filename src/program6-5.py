# プログラム6-5（初期条件2: phi2(x)）
u0 = 1; u1 = u0; u2 = 0.2 * u0; l1 = 2 * l; l2 = 0.2 * l
def u_init(x):
    return u1 * math.sin(2 * math.pi * x / l1) \
        + u2 * math.sin(2 * math.pi * x / l2)
