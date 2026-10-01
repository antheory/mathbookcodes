# プログラム6-18（共通するパラメーター）
ndim = 2 # 次元 (FDM, FEM, BEM, MC で共通)
u0 = 1.0 # 係数（境界条件の値を定義）
x0 = 0.0; x1 = 1.0; nx = 20
lx = x1 - x0; dx = lx / nx; dxdx = dx**2
y0 = 0.0; y1 = 1.0; ny = 20
ly = y1 - y0; dy = ly / ny; dydy = dy**2
