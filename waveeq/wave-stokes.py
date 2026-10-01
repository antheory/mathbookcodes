# wave-stokes.py 2026/10/01
# --+----1----+----2----+----3----+----4----+----5----+----6----+----7--
# 波動方程式の数値解（6.1.4 波動方程式の解，p.178）
#  (1) ストークスの公式の利用
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
# プログラム6-11（ストークスの公式で用いるphi(x)の奇関数の周期関数への拡張）
def u_init_odd(x):
    if x > 0.0:
        return u_init(x)
    else:
        return -u_init(-x)
def u_init_period(x):
    xtmp = x
    if xtmp > 0.0:
        while xtmp > l:
            xtmp -= 2.0 * l
    else:
        while xtmp < -l:
            xtmp += 2.0 * l
    return u_init_odd(xtmp)
# プログラム6-14（ストークスの公式による解）
for it in range(0, nt + 1): # 0<= it <= nt
    t = t0 + it * dt
    for ix in range(0, nx + 1): # 0 <= ix <= nx
        x = x0 + ix * dx
        u[ix] = (u_init_period(x - c * t) \
             + u_init_period(x + c * t)) / 2.0
    filename = "wave_{0:03d}.txt".format(it) # 出力部
    with open(filename, "w") as fone:
        for ix in range(0, nx + 1): # 0 <= ix <= nx
            x = x0 + ix * dx
            print(t, x, u[ix], file=fone)
