# プログラム6-36（BEM:内点の計算）
def calcus(px, py):
    us_in = 0.0
    for ie in range(nelem):
        a, b = setmatrixcomponents(ie, px, py)
        us_in += un[ie] * b - u[ie] * a
    us_in /= (2.0 * math.pi)
    return us_in
