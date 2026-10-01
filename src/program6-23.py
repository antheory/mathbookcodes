# プログラム6-23（MC:ランダムウォーク）
def randomwalk(ix_start, iy_start):
    ix_walk = ix_start
    iy_walk = iy_start
    ip_walk = (nx + 1) * iy_walk + ix_walk
    while i_bd[ip_walk] == 0: # 境界に達するまでランダムウォークする
        id = np.random.randint(0, 4)
        if id == 0:
            ix_walk -= 1
        elif id == 1:
            ix_walk += 1
        elif id == 2:
            iy_walk -= 1
        else:
            iy_walk += 1
        ip_walk = (nx + 1) * iy_walk + ix_walk
    ibd = i_bd[ip_walk] - 1 # 最終到達点を関数値として戻す
    return ibd
