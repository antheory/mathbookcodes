# wave-fourier.py 2026/10/01
# --+----1----+----2----+----3----+----4----+----5----+----6----+----7--
# 波動方程式の数値解（6.1.4 波動方程式の解，p.178）
#  (2) フーリエの方法
# 「機械工学のための数理モデリングと現象解析入門」
#   中谷彰宏著，2026年9月25日初版第1刷発行，コロナ社
#   (C) Akihiro Nakatani 2026
# --+----1----+----2----+----3----+----4----+----5----+----6----+----7--
# 関連するモジュールのインポート
import numpy as np
import math
import scipy
from scipy import integrate
# プログラム6-8改（座標・時間の範囲とパラメーターの設定）
x0 = 0.0; x1 = 1.0; nx = 50 # 境界，区間分割数
l = x1 - x0; dx = l / nx # 区間長
t0 = 0.0; t1 = 2.0; nt = 200 # 時間ステップ
dt = (t1 - t0) / nt # 時間増分
c = 1.0 # 波動伝ぱ速度
nmode = 100 # モード数
# プログラム6-9（配列要素の定義と初期化）
u = np.zeros(nx + 1); um = np.zeros(nx + 1)
f = np.zeros(nx + 1); An = np.zeros(nmode + 1)
# プログラム6-10（初期変位を表す関数phi(x)）
xa = 0.25; h = 1.0
def u_init(x):
    if x < xa:
        return h / xa * x
    else:
        return h * (l - x) / (l - xa)
# プログラム6-12（フーリエの方法で用いるフーリエ係数の計算）
def A_integrand(x, n):
    k = n * math.pi / l
    return u_init(x) * math.sin(k * x)
def A_fourier(n):
    val, _ = scipy.integrate.quad(A_integrand, x0, x1, args=(n))
    val *= 2 / l
    return val
for imode in range(1, nmode + 1): # 1 <= imode <= nmode
    An[imode] = A_fourier(imode)
# プログラム6-13（フーリエの方法で用いるモードnの解）
def u_phin(x, t, n):
    k = n * math.pi / l
    return An[n] * math.cos(c * k * t) * math.sin(k * x)
# プログラム6-15（フーリエの方法による解）
for it in range(0, nt + 1): # 0<= it <= nt
    t = t0 + it * dt
    for ix in range(0, nx + 1): # 0 <= ix <= nx
        x = x0 + ix * dx
        u[ix] = 0.0
        for imode in range(1, nmode + 1): # 1 <= imode <= nmode
            u[ix] += u_phin(x, t, imode)
    filename = "wave_{0:03d}.txt".format(it) # 出力部
    with open(filename, "w") as fone:
        for ix in range(0, nx + 1): # 0 <= ix <= nx
            x = x0 + ix * dx
            print(t, x, u[ix], file=fone)
