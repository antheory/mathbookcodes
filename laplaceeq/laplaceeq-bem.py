# laplaceeq-bem.py 2026/10/01
# --+----1----+----2----+----3----+----4----+----5----+----6----+----7--
# ラプラス方程式の数値解（6.2.6 解法の適用と結果の可視化，p.189）
#  (4) 境界要素法（FDM）
# 「機械工学のための数理モデリングと現象解析入門」
#   中谷彰宏著，2026年9月25日初版第1刷発行，コロナ社
#   (C) Akihiro Nakatani 2026
# --+----1----+----2----+----3----+----4----+----5----+----6----+----7--
# プログラム6-17（関連するモジュールのインポート）
import numpy as np
import math; DEBUG = False
# プログラム6-18（共通するパラメーター）
ndim = 2 # 次元 (FDM, FEM, BEM, MC で共通)
u0 = 1.0 # 係数（境界条件の値を定義）
x0 = 0.0; x1 = 1.0; nx = 20
lx = x1 - x0; dx = lx / nx; dxdx = dx**2
y0 = 0.0; y1 = 1.0; ny = 20
ly = y1 - y0; dy = ly / ny; dydy = dy**2
# プログラム6-30（BEM:境界要素の変数の宣言）
npe = 2  # 1要素当りの端点(BEM，線分)
npoin = 2 * (nx + ny) # 総端点数(BEM)
nelem = 2 * (nx + ny) # 総要素数(BEM，角点は共通)
u = np.zeros(nelem) # 境界値(BEM)
un = np.zeros(nelem) # 法線方向微分（BEM)
xe = np.zeros((nelem, ndim)) # 境界要素中心座標(BEM)
xp = np.zeros((npoin, ndim)) # 境界端点座標(BEM)
icon = np.zeros((nelem, npe), dtype=np.int64) # 要素端点の結合情報
i_bd = np.zeros(nelem, dtype=np.int64) # 境界のフラグ（0，非0）
v_bd = np.zeros(nelem) # 境界値
re = np.zeros(nelem) # 要素長さ
unx = np.zeros((nelem, ndim)) # 外向き法線ベクトル
# プログラム6-31（BEM:ルジャンドル・ガウス積分のパラメーター）
ng = 4 # 4点
xig = np.array([-0.86113631, -0.33998104, 0.33998104, 0.86113631])
wg = np.array([0.34785485, 0.65214515, 0.65214515, 0.34785485])
# プログラム6-32（BEM:境界条件）
def setbound1():
    for ie in range(0, nelem): # 全境界を同次ノイマン境界として初期化
        i_bd[ie] = 1
        v_bd[ie] = 0.0
    for ix in range(0, nx):     # 下部 iy = 0, y = y0上
        x = x0 + (ix + 0.5) * dx # 要素中央座標
        ie = ix
        i_bd[ie] = 0
        v_bd[ie] = u0 * math.sin(math.pi * x / lx)
    for iy in range(0, ny):     # 右部 ix = nx, x = x1上
        y = y0 + (iy + 0.5) * dy
        ie = nx + iy
        i_bd[ie] = 0
        v_bd[ie] = - u0 * math.sin(math.pi * y / ly)
    for ix in range(0, nx):     # 上部 iy = ny, y = y1上
        x = x1 - (ix + 0.5) * dx
        ie = (nx + ny) + ix
        i_bd[ie] = 0
        v_bd[ie] = u0 * math.sin(math.pi * x / lx)
    for iy in range(0, ny):     # 左部　ix = 0, x = x0上
        y = y1 - (iy + 0.5) * dy
        ie = 2 * nx + ny + iy
        i_bd[ie] = 0
        v_bd[ie] = - u0 * math.sin(math.pi * y / ly)
    if DEBUG:
        for ie in range(0, nelem):
            print (ie, i_bd[ie], v_bd[ie])
# プログラム6-33（BEM:境界要素の端点）
def setedgenode(): # 反時計まわりに番号付け
    ip = 0
    for ix in range(0, nx):
        xp[ip][0] = x0 + ix * dx
        xp[ip][1] = y0
        ip += 1
    for iy in range(0, ny):
        xp[ip][0] = x1
        xp[ip][1] = y0 + iy * dy
        ip += 1
    for ix in range(0, nx):
        xp[ip][0] = x1 - ix * dx
        xp[ip][1] = y1
        ip += 1
    for iy in range(0, ny):
        xp[ip][0] = x0
        xp[ip][1] = y1 - iy * dy
        ip += 1
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
# プログラム6-36（BEM:内点の計算）
def calcus(px, py):
    us_in = 0.0
    for ie in range(nelem):
        a, b = setmatrixcomponents(ie, px, py)
        us_in += un[ie] * b - u[ie] * a
    us_in /= (2.0 * math.pi)
    return us_in
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
