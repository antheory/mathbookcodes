# プログラム6-19（変数の定義など (BEM 以外，必要に応じて)）
# 計算に関係する定数
penalty = 1e8 # 大きな数 (FEM)
nwalk = 1000 # ランダムウォークの数 (MC)
# 離散化に関連するパラメーター
npe = 3 # 1要素当りの節点数 (FEM，三角形要素)
npoin = (nx + 1) * (ny + 1) # 総節点数 (FEM)，格子点数 (FDM, MC)
nelem = 2 * nx * ny # 総要素数 (FEM)
u = np.zeros(npoin) # 未知関数 (FEM，FDM, MC)
xp = np.zeros((npoin, ndim)) # 節点座標 (FEM)
icon = np.zeros((nelem, npe), dtype=np.int64) #要素節点接続性 (FEM)
# 境界条件のフラグ設定（FDM, FEM, MC）
i_bd = np.zeros(npoin, dtype=np.int64) # 0 で内部，1 以上で境界番号
v_bd = np.zeros(npoin) # 境界値
