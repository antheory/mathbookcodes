# プログラム6-32（BEM:境界条件）
def setbound1():
    for ie in range(0, nelem): # 全境界を同次ノイマン境界として初期化
        i_bd[ie] = 1
        v_bd[ie] = 0.0
    for ix in range(0, nx):     # 下部 iy = 0, y = y0上
        x = x0 + (ix + 0.5) * dx # 要素中央座標
        ie = ix
        i_bd[ie] = 0
        v_bd[ie] = u0 * math.sin(math.pi * x / lx)
    for iy in range(0, ny):     # 右部 ix = nx, x = x1上
        y = y0 + (iy + 0.5) * dy
        ie = nx + iy
        i_bd[ie] = 0
        v_bd[ie] = - u0 * math.sin(math.pi * y / ly)
    for ix in range(0, nx):     # 上部 iy = ny, y = y1上
        x = x1 - (ix + 0.5) * dx
        ie = (nx + ny) + ix
        i_bd[ie] = 0
        v_bd[ie] = u0 * math.sin(math.pi * x / lx)
    for iy in range(0, ny):     # 左部　ix = 0, x = x0上
        y = y1 - (iy + 0.5) * dy
        ie = 2 * nx + ny + iy
        i_bd[ie] = 0
        v_bd[ie] = - u0 * math.sin(math.pi * y / ly)
    if DEBUG:
        for ie in range(0, nelem):
            print (ie, i_bd[ie], v_bd[ie])
