# プログラム6-26（FEM:要素作成と要素節点接続性の設定）
def setelem(): # 三角形要素に分割
    for iy in range(0, ny):
        for ix in range(0, nx):
            ielem = (2 * nx) * iy + 2 * ix
            icon[ielem][0] = (nx + 1) * iy + ix
            icon[ielem][1] = (nx + 1) * iy + ix + 1
            icon[ielem][2] = (nx + 1) * (iy + 1) + ix + 1
            ielem = (2 * nx) * iy + 2 * ix + 1
            icon[ielem][0] = (nx + 1) * iy + ix
            icon[ielem][1] = (nx + 1) * (iy + 1) + ix + 1
            icon[ielem][2] = (nx + 1) * (iy + 1) + ix
