# プログラム6-20（ディリクレ境界条件 (BEM 以外)）
def setbound1():
    iy = 0 # y = y0 上
    for ix in range(0, nx + 1):
        x = x0 + ix * dx
        ip = (nx + 1) * iy + ix
        i_bd[ip] = 1
        v_bd[ip] = u0 * math.sin(math.pi * x / lx)
    iy = ny # y = y1 上
    for ix in range(0, nx + 1):
        x = x0 + ix * dx
        ip = (nx + 1) * iy + ix
        i_bd[ip] = 1
        v_bd[ip] = u0 * math.sin(math.pi * x / lx)
    ix = 0 # x = x0 上
    for iy in range(0, ny + 1):
        y = y0 + iy * dy
        ip = (nx + 1) * iy + ix
        i_bd[ip] = 1
        v_bd[ip] = - u0 * math.sin(math.pi * y / ly)
    ix = nx # x = x1 上
    for iy in range(0, ny + 1):
        y = y0 + iy * dy
        ip = (nx + 1) * iy + ix
        i_bd[ip] = 1
        v_bd[ip] = - u0 * math.sin(math.pi * y / ly)
    nbd = 0 # 境界点の総数のカウント
    for ip in range(0, npoin):
        if i_bd[ip] != 0:
            nbd += 1
    return nbd
