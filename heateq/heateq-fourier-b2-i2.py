# heateq-fourier-b2-i2.py 2026/10/01
# --+----1----+----2----+----3----+----4----+----5----+----6----+----7--
# 熱伝導方程式の数値解（6.1.3 熱伝導・拡散方程式の解，p.173）
#  (1) フーリエの方法による計算
#  境界条件2：ノイマン境界条件
#  初期条件2：正弦波形
# 「機械工学のための数理モデリングと現象解析入門」
#   中谷彰宏著，2026年9月25日初版第1刷発行，コロナ社
#   (C) Akihiro Nakatani 2026
# --+----1----+----2----+----3----+----4----+----5----+----6----+----7--
# 関連するモジュールのインポート
import numpy as np
import math
# プログラム6-1（座標・時間の範囲とパラメーターの設定）
x0 = 0.0; x1 = 1.0; nx = 50 # 境界，区間分割数
l = x1 - x0; dx = l / nx # 格子間隔
t0 = 0.0; t1 = 2.0; nt = 200 # ステップ数
dt = (t1 - t0) / nt # 時間増分
ckappa = 2.0e-2 # 定数
nmode = 100 # モード数 (フーリエの方法)
import scipy.integrate # モジュールのインポート
# プログラム6-3（境界条件2: ノイマン問題の場合）
imode_ini = 0
def A_integrand(x, n):
    k = n * math.pi / l
    return u_init(x) * math.cos(k * x)
def A_fourier(n):
    val, _ = scipy.integrate.quad(A_integrand, x0, x1, args=(n,))
    if n == 0:
        val *= 1 / l
    else:
        val *= 2 / l
    return val
def u_phin(x, t, n):
    k = n * math.pi / l
    return An[n] * math.exp(- ckappa * k**2 * t) * math.cos(k * x)
# プログラム6-5（初期条件2: phi2(x)）
u0 = 1; u1 = u0; u2 = 0.2 * u0; l1 = 2 * l; l2 = 0.2 * l
def u_init(x):
    return u1 * math.sin(2 * math.pi * x / l1) \
        + u2 * math.sin(2 * math.pi * x / l2)
# プログラム6-6（フーリエの方法の計算例）
An = np.zeros(nmode + 1)
for imode in range(imode_ini, nmode + 1):
    An[imode] = A_fourier(imode)
t = 0.0
for imode in range(imode_ini, nmode + 1):
    filename = "fmode1_{0:03d}.txt".format(imode)
    with open(filename, "w") as fmode:
        for ix in range(0, nx + 1): # 0 <= ix <= nx
            x = x0 + ix * dx
            print(t, x, u_phin(x, t, imode), file=fmode)
u = np.zeros(nx +1)
with open("fourier1.txt", "w") as fall, \
     open("fourier1_energy.txt", "w") as fenergy, \
     open("fourier1_every.txt", "w") as fevery:
    for it in range(0, nt + 1): # 0<= it <= nt
        t = t0 + it * dt
        for ix in range(0, nx + 1): # 0 <= ix <= nx
            x = x0 + ix * dx
            u[ix] = 0.0
            for imode in range(imode_ini, nmode + 1):
                u[ix] += u_phin(x, t, imode)
        filename = "fourier1_{0:03d}.txt".format(it)
        with open(filename, "w") as fone:
            energy = (np.sum(u) - u[0] / 2.0 - u[nx] / 2.0) * dx
            print(t, energy, file=fenergy)
            for ix in range(0, nx + 1): # 0 <= ix <= nx
                x = x0 + ix * dx
                print(t, x, u[ix], file=fone)
                print(t, x, u[ix], file=fall)
                if it % 10 == 0:
                    print(t, x, u[ix], file=fevery)
        print(file=fall)
        if it % 10 == 0:
            print(file=fevery)
