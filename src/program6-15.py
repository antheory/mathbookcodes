# プログラム6-15（フーリエの方法による解）
for it in range(0, nt + 1): # 0<= it <= nt
    t = t0 + it * dt
    for ix in range(0, nx + 1): # 0 <= ix <= nx
        x = x0 + ix * dx
        u[ix] = 0.0
        for imode in range(1, nmode + 1): # 1 <= imode <= nmode
            u[ix] += u_phin(x, t, imode)
