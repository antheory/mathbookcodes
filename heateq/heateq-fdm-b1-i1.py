# heateq-fdm-b1-i1.py 2026/10/01
# --+----1----+----2----+----3----+----4----+----5----+----6----+----7--
# 熱伝導方程式の数値解（6.1.3 熱伝導・拡散方程式の解，p.173）
#  (2) 差分法を用いた解析
#  境界条件1：ディリクレ境界条件
#  初期条件1：矩形波形
# 「機械工学のための数理モデリングと現象解析入門」
#   中谷彰宏著，2026年9月25日初版第1刷発行，コロナ社
#   (C) Akihiro Nakatani 2026
# --+----1----+----2----+----3----+----4----+----5----+----6----+----7--
# 関連するモジュールのインポート
import numpy as np
# プログラム6-1改（座標・時間の範囲とパラメーターの設定）
x0 = 0.0; x1 = 1.0; nx = 50 # 境界，区間分割数
l = x1 - x0; dx = l / nx # 格子間隔
t0 = 0.0; t1 = 2.0; nt = 200 # ステップ数
dt = (t1 - t0) / nt # 時間増分
ckappa = 2.0e-2 # 定数
# プログラム6-4（初期条件1: phi1(x)）
xa = 0.25 * l; u0 = 1.0   #   a = l / 4 の場合
def u_init(x):
    if x < xa:
        return 0
    elif x < (l-xa):
        return u0
    else:
        return 0
# プログラム6-7改（差分法の計算例）ディリクレ境界条件
coef = ckappa * dt / dx**2 # 差分法の係数
t = 0.0; u = np.zeros(nx + 1)
for ix in range(0, nx + 1): # 0<= ix <= nx
    u[ix] = u_init(x0 + ix * dx)
du = np.zeros(nx + 1)
with open("fdm1.txt", "w") as fall, \
     open("fdm1_energy.txt", "w") as fenergy, \
     open("fdm1_every.txt", "w") as fevery:
    it = 0
    with open("fdm1_{0:03d}.txt".format(it), "w") as fone:
        for ix in range(0, nx + 1): # 0<= ix <= nx
            x = x0 + ix * dx
            print (t, x, u[ix], file=fall)
            print(t, x, u[ix], file=fone)
            print(t, x, u[ix], file=fevery)
    print(file=fevery)
    print(file=fall)
    print(t, (np.sum(u) - u[0]/2 - u[nx]/2) * dx, file=fenergy)
    for it in range(1, nt + 1): # 1 <= it <= nt
# ディリクレ境界条件
        for ix in range(1, nx): # 1 <= ix <= nx - 1
            du[ix] = coef * (u[ix + 1] + u[ix - 1] - 2.0 * u[ix])
        for ix in range(1, nx): # 1 <= ix <= nx - 1
            u[ix] += du[ix]
# ノイマン境界条件（コメントアウトにより保留）
#       du[0] = coef * (2.0 * u[1] - 2.0 * u[0])
#       for ix in range(1, nx): # 1 <= ix <= nx - 1
#           du[ix] = coef * (u[ix + 1] + u[ix - 1] - 2.0 * u[ix])
#       du[nx] = coef * (2.0 * u[nx - 1] - 2.0 * u[nx])
#       for ix in range(0, nx + 1): # 0 <= ix <= nx
#           u[ix] += du[ix]
        t += dt
        filename = "fdm1_{0:03d}.txt".format(it)
        with open(filename, "w") as fone:
            print(t, (np.sum(u) - u[0]/2 - u[nx]/2) * dx, \
                file=fenergy)
            for ix in range(0, nx + 1): # 0 <= ix <= nx
                x = x0 + ix * dx
                print(t, x, u[ix], file=fone)
                print(t, x, u[ix], file=fall)
                if it % 10 == 0:
                    print(t, x, u[ix], file=fevery)
        print(file=fall)
        if it % 10 == 0:
            print(file=fevery)
