# プログラム6-14（ストークスの公式による解）
for it in range(0, nt + 1): # 0<= it <= nt
    t = t0 + it * dt
    for ix in range(0, nx + 1): # 0 <= ix <= nx
        x = x0 + ix * dx
        u[ix] = (u_init_period(x - c * t) \
             + u_init_period(x + c * t)) / 2.0
