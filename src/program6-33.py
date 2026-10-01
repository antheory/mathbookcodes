# プログラム6-33（BEM:境界要素の端点）
def setedgenode(): # 反時計まわりに番号付け
    ip = 0
    for ix in range(0, nx):
        xp[ip][0] = x0 + ix * dx
        xp[ip][1] = y0
        ip += 1
    for iy in range(0, ny):
        xp[ip][0] = x1
        xp[ip][1] = y0 + iy * dy
        ip += 1
    for ix in range(0, nx):
        xp[ip][0] = x1 - ix * dx
        xp[ip][1] = y1
        ip += 1
    for iy in range(0, ny):
        xp[ip][0] = x0
        xp[ip][1] = y1 - iy * dy
        ip += 1
