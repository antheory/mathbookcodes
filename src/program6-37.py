# プログラム6-37（BEM:メインルーチン）
setbound1()
setedgenode()
setelem()
amat = np.zeros((nelem, nelem))
bmat = np.zeros((nelem, nelem))
rhs = np.zeros(nelem)
for ie1 in range(0, nelem):
    for ie2 in range(0, nelem):
        if ie1 == ie2: # 対角項の特異積分は解析解を用いる
            ie = ie2
            amat[ie][ie] = math.pi
            bmat[ie][ie] = re[ie] * (1.0 - math.log(re[ie] / 2.0))
        else:
            amat[ie1][ie2], bmat[ie1][ie2] = (setmatrixcomponents(
                ie2, xe[ie1][0], xe[ie1][1])
            )
# ディリクレ条件について未知量uをunに入れ替え
for ie2 in range(0, nelem):
    if i_bd[ie2] == 0:
        for ie1 in range(0, nelem):
            work = bmat[ie1][ie2]
            bmat[ie1][ie2] = - amat[ie1][ie2]
            amat[ie1][ie2] = - work
for ie1 in range(0, nelem): # 連立1次方程式の右辺
    rhs[ie1] = 0
    for ie2 in range(0, nelem):
         rhs[ie1] += bmat[ie1][ie2] * v_bd[ie2]
u = np.linalg.solve(amat, rhs)  # 連立1次方程式
# 解の物理的な解釈を境界条件に合わせる
for ie in range(0, nelem):
    if i_bd[ie] == 0:
        un[ie] = u[ie]
        u[ie] = v_bd[ie]
    else:
        un[ie] = v_bd[ie]
# 内点の関数値の評価
with open("fbemall.txt", "w") as fall:
    for iy in range(1, ny):
        y = y0 + iy * dy
        for ix in range(1, nx):
            x = x0 + ix * dx
            us_in = calcus(x, y)
            print (x, y, us_in, file=fall)
        print (file=fall)
