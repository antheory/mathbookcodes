# laplaceeq-fdm.py 2026/10/01
# --+----1----+----2----+----3----+----4----+----5----+----6----+----7--
# ラプラス方程式の数値解（6.2.6 解法の適用と結果の可視化，p.189）
#  (1) 差分法（FDM）
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
# プログラム6-19改（変数の定義など (FDM)）
# 離散化に関連するパラメーター
npoin = (nx + 1) * (ny + 1) # 格子点数 (FDM)
u = np.zeros(npoin) # 未知関数 (FDM)
# 境界条件のフラグ設定（FDM）
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
# プログラム6-22（FDM:メインルーチン）
nbd = setbound1()
ip_bd = np.zeros(nbd, dtype=np.int64) # 境界点のリスト
setbound2()
A = np.zeros((npoin, npoin))
b = np.zeros(npoin)
for iy in range(0, ny + 1):
    for ix in range(0, nx + 1):
        ip = (nx + 1) * iy + ix
        if i_bd[ip] == 0: # 内部の点のみに離散ラプラシアンを適用
            A[ip][ip] = - (2.0 / dxdx + 2.0 / dydy)
            ip_x_p = (nx + 1) * iy + ix + 1
            if i_bd[ip_x_p] == 0:
                A[ip_x_p][ip] = 1.0 / dxdx
            else:
                A[ip_x_p][ip] = (1.0 / dxdx) * 0.0
                b[ip] += - 1.0 / dxdx * v_bd[ip_x_p]
            ip_x_m = (nx + 1) * iy + ix - 1
            if i_bd[ip_x_m] == 0:
                A[ip_x_m][ip] = 1.0 / dxdx
            else:
                A[ip_x_m][ip] = (1.0 / dxdx) * 0.0
                b[ip] += - 1.0 / dxdx * v_bd[ip_x_m]
            ip_y_p = (nx + 1) * (iy + 1) + ix 
            if i_bd[ip_y_p] == 0:
                A[ip_y_p][ip] = 1.0 / dydy
            else:
                A[ip_y_p][ip] = (1.0 / dydy) * 0.0
                b[ip] += - 1.0 / dydy * v_bd[ip_y_p]
            ip_y_m = (nx + 1) * (iy - 1) + ix
            if i_bd[ip_y_m] == 0:
                A[ip_y_m][ip] = 1.0 / dydy
            else:
                A[ip_y_m][ip] = (1.0 / dydy) * 0.0
                b[ip] += - 1.0 / dydy * v_bd[ip_y_m]
for ibd in range(0, nbd): # ディリクレ境界の値の設定
    ip = ip_bd[ibd]
    A[ip][ip] = - (2.0 / dxdx + 2.0 / dydy)
    b[ip] = A[ip][ip] * v_bd[ip]
u = np.linalg.solve(A, b)   # 連立一次方程式
# プログラム6-29改（解の出力(FDMの例)）
with open("ffdmall.txt", "w") as fall:
    for iy in range(0, ny + 1):
        y = y0 + iy * dy
        for ix in range(0, nx + 1):
            x = x0 + ix * dx
            ip = (nx + 1) * iy + ix
            print(x, y, u[ip], file=fall)
        print (file=fall)
