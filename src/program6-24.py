# プログラム6-24（MC:メインルーチン）
nbd = setbound1()
ip_bd = np.zeros(nbd, dtype=np.int64) # 境界点のリスト
ipr_bd = np.zeros(nbd, dtype=np.int64) # 各境界点への到達数
setbound2()
with open("fMonteCarloall.txt", "w") as fall:
    for iy in range(0, ny + 1):
        y = y0 + iy * dy
        for ix in range(0, nx + 1):
            x = x0 + ix * dx
            ip = (nx + 1) * iy + ix
            for ibd in range(0, nbd):
                ipr_bd[ibd] = 0
            for iwalk in range(0, nwalk): # ランダムウォーク
                ibd = randomwalk(ix,iy)
                ipr_bd[ibd] += 1
            u[ip] = 0.0 # ここから解の評価
            for ibd in range(0, nbd):
                u[ip] += float(ipr_bd[ibd]) \
                    / float(nwalk) * v_bd[ip_bd[ibd]]
            print(x, y, u[ip], file=fall)
        print(file=fall)
