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
