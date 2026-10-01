# wave-fdm.py 2026/10/01
# --+----1----+----2----+----3----+----4----+----5----+----6----+----7--
# 波動方程式の数値解（6.1.4 波動方程式の解，p.178）
#  (3) 差分法
# 「機械工学のための数理モデリングと現象解析入門」
#   中谷彰宏著，2026年9月25日初版第1刷発行，コロナ社
#   (C) Akihiro Nakatani 2026
# --+----1----+----2----+----3----+----4----+----5----+----6----+----7--
# 関連するモジュールのインポート
import numpy as np
# プログラム6-8（座標・時間の範囲とパラメーターの設定）
x0 = 0.0; x1 = 1.0; nx = 50 # 境界，区間分割数
l = x1 - x0; dx = l / nx # 区間長
t0 = 0.0; t1 = 2.0; nt = 200 # 時間ステップ
dt = (t1 - t0) / nt # 時間増分
c = 1.0 # 波動伝ぱ速度
# プログラム6-9改（配列要素の定義と初期化）
u = np.zeros(nx + 1); um = np.zeros(nx + 1)
f = np.zeros(nx + 1)
# プログラム6-10（初期変位を表す関数phi(x)）
xa = 0.25; h = 1.0
def u_init(x):
    if x < xa:
        return h / xa * x
    else:
        return h * (l - x) / (l - xa)
# プログラム6-16（差分法による解）
coef = (c * dt / dx) ** 2 # クーラン数の2乗
for ix in range(0, nx + 1): # 0<= ix <= nx # 初期値の代入
    u[ix] = u_init(x0 + ix * dx)
um[0] = 0.0 # 1ステップ前の値の評価
for ix in range(1, nx): # 1<= ix <= nx - 1
    um[ix] = u[ix] + 0.5 * \
        coef * (u[ix + 1] + u[ix - 1] - 2.0 * u[ix])
um[nx] = 0.0; t = t0
for it in range(1, nt + 1): # 1 <= it <= nt
    for ix in range(1, nx): # 1 <= ix <= nx - 1
        f[ix] = - um[ix] + coef * \
            (u[ix + 1] + u[ix - 1] - 2.0 * u[ix])
    um[:] = u[:] # update displacement of the previous time step
    for ix in range(1, nx): # 1 <= ix <= nx - 1
        u[ix] = 2.0 * u[ix] + f[ix]
    t += dt
    filename = "wave_{0:03d}.txt".format(it) # 出力部
    with open(filename, "w") as fone:
        for ix in range(0, nx + 1): # 0 <= ix <= nx
            x = x0 + ix * dx
            print(t, x, u[ix], file=fone)
