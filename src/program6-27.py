# プログラム6-27（FEM:内挿関数の偏導関数）
def dshape(xpe):
    fd = np.zeros((ndim, npe))
    x = 0; y = 1
    ie1 = 0; ie2 = 1; ie3 = 2
    area2 = (
        xpe[ie2][x] * xpe[ie3][y] - xpe[ie2][y] * xpe[ie3][x]
        + xpe[ie3][x] * xpe[ie1][y] - xpe[ie3][y] * xpe[ie1][x]
        + xpe[ie1][x] * xpe[ie2][y] - xpe[ie1][y] * xpe[ie2][x]
    )
    fd[x][ie1] = (xpe[ie2][y] - xpe[ie3][y]) / area2
    fd[y][ie1] = (xpe[ie3][x] - xpe[ie2][x]) / area2
    fd[x][ie2] = (xpe[ie3][y] - xpe[ie1][y]) / area2
    fd[y][ie2] = (xpe[ie1][x] - xpe[ie3][x]) / area2
    fd[x][ie3] = (xpe[ie1][y] - xpe[ie2][y]) / area2
    fd[y][ie3] = (xpe[ie2][x] - xpe[ie1][x]) / area2
    area = area2 / 2.0
    return area, fd # 要素面積と内挿関数の偏導関数を戻す
