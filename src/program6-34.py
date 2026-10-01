# プログラム6-34（BEM:要素端点接続性の設定）
def setelem():
    for ie in range(0, nelem):
        ip = ie
        icon[ie][0] = ip
        icon[ie][1] = (ip + 1) % npoin
    for ie in range(0, nelem):
        ip0 = icon[ie][0]
        ip1 = icon[ie][1]
        for idim in range(0, ndim):
            xe[ie][idim] = (xp[ip0][idim] + xp[ip1][idim]) * 0.5
        sx0 = xp[ip1][0] - xp[ip0][0] # 接線ベクトル x成分
        sx1 = xp[ip1][1] - xp[ip0][1] # 接線ベクトル y成分
        re[ie] = math.sqrt(sx0**2 + sx1**2) # 要素長さ
        unx[ie][0] = sx1 / re[ie] # 外向き法線ベクトル x成分
        unx[ie][1] = - sx0 / re[ie] # 外向き法線ベクトル y成分
