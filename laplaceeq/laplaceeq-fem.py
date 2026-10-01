# laplaceeq-fem.py 2026/10/01
# --+----1----+----2----+----3----+----4----+----5----+----6----+----7--
# ラプラス方程式の数値解（6.2.6 解法の適用と結果の可視化，p.189）
#  (3) 有限要素法（FEM）
# 「機械工学のための数理モデリングと現象解析入門」
#   中谷彰宏著，2026年9月25日初版第1刷発行，コロナ社
#   (C) Akihiro Nakatani 2026
# --+----1----+----2----+----3----+----4----+----5----+----6----+----7--
# プログラム6-17改（関連するモジュールのインポート）
import numpy as np
import math
# プログラム6-18（共通するパラメーター）
ndim = 2 # 次元 (FDM, FEM, BEM, MC で共通)
u0 = 1.0 # 係数（境界条件の値を定義）
x0 = 0.0; x1 = 1.0; nx = 20
lx = x1 - x0; dx = lx / nx; dxdx = dx**2
y0 = 0.0; y1 = 1.0; ny = 20
ly = y1 - y0; dy = ly / ny; dydy = dy**2
# プログラム6-19改（変数の定義など (FEM)）
# 計算に関係する定数
penalty = 1e8 # 大きな数 (FEM)
# 離散化に関連するパラメーター
npe = 3 # 1要素当りの節点数 (FEM，三角形要素)
npoin = (nx + 1) * (ny + 1) # 総節点数 (FEM)
nelem = 2 * nx * ny # 総要素数 (FEM)
u = np.zeros(npoin) # 未知関数 (FEM)
xp = np.zeros((npoin, ndim)) # 節点座標 (FEM)
icon = np.zeros((nelem, npe), dtype=np.int64) #要素節点接続性 (FEM)
# 境界条件のフラグ設定（FEM）
i_bd = np.zeros(npoin, dtype=np.int64) # 0 で内部，1 以上で境界番号
v_bd = np.zeros(npoin) # 境界値
# プログラム6-20改（ディリクレ境界条件）
def setbound1():
    iy = 0 # y = y0 上
    for ix in range(0, nx + 1):
        x = x0 + ix * dx
        ip = (nx + 1) * iy + ix
        i_bd[ip] = 1
        v_bd[ip] = u0 * math.sin(math.pi * x / lx)
    iy = ny # y = y1 上
    for ix in range(0, nx + 1):
        x = x0 + ix * dx
        ip = (nx + 1) * iy + ix
        i_bd[ip] = 1
        v_bd[ip] = u0 * math.sin(math.pi * x / lx)
    ix = 0 # x = x0 上
    for iy in range(0, ny + 1):
        y = y0 + iy * dy
        ip = (nx + 1) * iy + ix
        i_bd[ip] = 1
        v_bd[ip] = - u0 * math.sin(math.pi * y / ly)
    ix = nx # x = x1 上
    for iy in range(0, ny + 1):
        y = y0 + iy * dy
        ip = (nx + 1) * iy + ix
        i_bd[ip] = 1
        v_bd[ip] = - u0 * math.sin(math.pi * y / ly)
    nbd = 0 # 境界点の総数のカウント
    for ip in range(0, npoin):
        if i_bd[ip] != 0:
            nbd += 1
    return nbd
# プログラム6-21（ディリクレ境界の番号登録）
def setbound2():
    ibd = 0
    for ip in range(0, npoin):
        if i_bd[ip] != 0:
            i_bd[ip] = ibd + 1
            ip_bd[ibd] = ip
            ibd += 1
# プログラム6-25（FEM:節点の生成）
def setnode():
     ip = 0
     for iy in range(0, ny + 1):
          for ix in range(0, nx + 1):
               xp[ip][0] = x0 + ix * dx
               xp[ip][1] = y0 + iy * dy
               ip += 1
# プログラム6-26（FEM:要素作成と要素節点接続性の設定）
def setelem(): # 三角形要素に分割
    for iy in range(0, ny):
        for ix in range(0, nx):
            ielem = (2 * nx) * iy + 2 * ix
            icon[ielem][0] = (nx + 1) * iy + ix
            icon[ielem][1] = (nx + 1) * iy + ix + 1
            icon[ielem][2] = (nx + 1) * (iy + 1) + ix + 1
            ielem = (2 * nx) * iy + 2 * ix + 1
            icon[ielem][0] = (nx + 1) * iy + ix
            icon[ielem][1] = (nx + 1) * (iy + 1) + ix + 1
            icon[ielem][2] = (nx + 1) * (iy + 1) + ix
# プログラム6-27（FEM:内挿関数の偏導関数）
def dshape(xpe):
    fd = np.zeros((ndim, npe))
    x = 0; y = 1
    ie1 = 0; ie2 = 1; ie3 = 2
    area2 = (
        xpe[ie2][x] * xpe[ie3][y] - xpe[ie2][y] * xpe[ie3][x]
        + xpe[ie3][x] * xpe[ie1][y] - xpe[ie3][y] * xpe[ie1][x]
        + xpe[ie1][x] * xpe[ie2][y] - xpe[ie1][y] * xpe[ie2][x]
    )
    fd[x][ie1] = (xpe[ie2][y] - xpe[ie3][y]) / area2
    fd[y][ie1] = (xpe[ie3][x] - xpe[ie2][x]) / area2
    fd[x][ie2] = (xpe[ie3][y] - xpe[ie1][y]) / area2
    fd[y][ie2] = (xpe[ie1][x] - xpe[ie3][x]) / area2
    fd[x][ie3] = (xpe[ie1][y] - xpe[ie2][y]) / area2
    fd[y][ie3] = (xpe[ie2][x] - xpe[ie1][x]) / area2
    area = area2 / 2.0
    return area, fd # 要素面積と内挿関数の偏導関数を戻す
# プログラム6-28（FEM:メインルーチン）
nbd = setbound1()
ip_bd = np.zeros(nbd, dtype=np.int64)
setbound2()
setnode()
setelem()
xpe = np.zeros((npe, ndim))  # 要素節点座標
fd = np.zeros((ndim, npe))   # 内挿関数の導関数
Aelm = np.zeros((npe, npe))  # 要素剛性マトリクス
A = np.zeros((npoin, npoin)) # 全体剛性マトリクス
b = np.zeros(npoin)          # 連立1次方程式の右辺
for ielem in range(0, nelem):
    for ipe in range(0, npe):
        for idim in range(0, ndim):
            xpe[ipe][idim] = xp[icon[ielem][ipe]][idim]
    area, fd = dshape(xpe)
    Aelm = area * np.dot(np.transpose(fd), fd)
    for ipe2 in range(0, npe):
        for ipe1 in range(0, npe):
            ip1 = icon[ielem][ipe1]
            ip2 = icon[ielem][ipe2]
            A[ip1][ip2] += Aelm[ipe1][ipe2]
for ibd in range(0, nbd):
    ip = ip_bd[ibd]
    A[ip][ip] += penalty
    b[ip] += penalty * v_bd[ip]
u = np.linalg.solve(A, b)  # 連立1次方程式
# プログラム6-29改（解の出力(FEMの例)）
with open("ffemall.txt", "w") as fall:
    for iy in range(0, ny + 1):
        y = y0 + iy * dy
        for ix in range(0, nx + 1):
            x = x0 + ix * dx
            ip = (nx + 1) * iy + ix
            print(x, y, u[ip], file=fall)
        print (file=fall)
