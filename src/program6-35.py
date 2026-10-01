# プログラム6-35（BEM:境界積分による影響係数の計算）
def setmatrixcomponents(ie, px, py):
    ip0 = icon[ie][0]
    ip1 = icon[ie][1]
    sx0 = xp[ip1][0] - xp[ip0][0]
    sx1 = xp[ip1][1] - xp[ip0][1]
    a = 0.0
    b = 0.0
    for ig in range(0, ng): # ガウス積分
        xg = xe[ie][0] + sx0 / 2.0 * xig[ig]
        yg = xe[ie][1] + sx1 / 2.0 * xig[ig]
        rm = math.sqrt((xg - px) ** 2 + (yg - py) ** 2)
        a += -(
            unx[ie][0] * (xg - px) + unx[ie][1] * (yg - py)
        ) / rm**2 * wg[ig] * (re[ie] / 2.0)
        b += -math.log(rm) * wg[ig] * (re[ie] / 2.0)
    return a, b # uについての係数aとunについての係数bを戻す
