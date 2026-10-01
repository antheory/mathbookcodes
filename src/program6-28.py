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
