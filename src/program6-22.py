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
                A[ip][ip_x_p] = 1.0 / dxdx
            else:
                A[ip][ip_x_p] = (1.0 / dxdx) * 0.0
                b[ip] += - 1.0 / dxdx * v_bd[ip_x_p]
            ip_x_m = (nx + 1) * iy + ix - 1
            if i_bd[ip_x_m] == 0:
                A[ip][ip_x_m] = 1.0 / dxdx
            else:
                A[ip][ip_x_m] = (1.0 / dxdx) * 0.0
                b[ip] += - 1.0 / dxdx * v_bd[ip_x_m]
            ip_y_p = (nx + 1) * (iy + 1) + ix 
            if i_bd[ip_y_p] == 0:
                A[ip][ip_y_p] = 1.0 / dydy
            else:
                A[ip][ip_y_p] = (1.0 / dydy) * 0.0
                b[ip] += - 1.0 / dydy * v_bd[ip_y_p]
            ip_y_m = (nx + 1) * (iy - 1) + ix
            if i_bd[ip_y_m] == 0:
                A[ip][ip_y_m] = 1.0 / dydy
            else:
                A[ip][ip_y_m] = (1.0 / dydy) * 0.0
                b[ip] += - 1.0 / dydy * v_bd[ip_y_m]
for ibd in range(0, nbd): # ディリクレ境界の値の設定
    ip = ip_bd[ibd]
    A[ip][ip] = - (2.0 / dxdx + 2.0 / dydy)
    b[ip] = A[ip][ip] * v_bd[ip]
u = np.linalg.solve(A, b)   # 連立一次方程式
