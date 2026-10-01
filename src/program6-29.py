# プログラム6-29（解の出力(FEMの例，FDMも同様)）
with open("ffemall.txt", "w") as fall:
    for iy in range(0, ny + 1):
        y = y0 + iy * dy
        for ix in range(0, nx + 1):
            x = x0 + ix * dx
            ip = (nx + 1) * iy + ix
            print(x, y, u[ip], file=fall)
        print (file=fall)
