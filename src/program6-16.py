# プログラム6-16（差分法による解）
coef = (c * dt / dx) ** 2 # クーラン数の2乗
for ix in range(0, nx + 1): # 0<= ix <= nx # 初期値の代入
    u[ix] = u_init(x0 + ix * dx)
um[0] = 0.0 # 1ステップ前の値の評価
for ix in range(1, nx): # 1<= ix <= nx - 1
    um[ix] = u[ix] + 0.5 * \
        coef * (u[ix + 1] + u[ix - 1] - 2.0 * u[ix])
um[nx] = 0.0; t = t0
for it in range(1, nt + 1): # 1 <= it <= nt
    for ix in range(1, nx): # 1 <= ix <= nx - 1
        f[ix] = - um[ix] + coef * \
            (u[ix + 1] + u[ix - 1] - 2.0 * u[ix])
    um[:] = u[:] # update displacement of the previous time step
    for ix in range(1, nx): # 1 <= ix <= nx - 1
        u[ix] = 2.0 * u[ix] + f[ix]
    t += dt
