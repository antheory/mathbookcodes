# プログラム6-7（差分法の計算例）
coef = ckappa * dt / dx**2 # 差分法の係数
t = 0.0; u = np.zeros(nx + 1)
for ix in range(0, nx + 1): # 0<= ix <= nx
    u[ix] = u_init(x0 + ix * dx)
du = np.zeros(nx + 1)
with open("fdm1.txt", "w") as fall, \
     open("fdm1_energy.txt", "w") as fenergy, \
     open("fdm1_every.txt", "w") as fevery:
    it = 0
    with open("fdm1_{0:03d}.txt".format(it), "w") as fone:
        for ix in range(0, nx + 1): # 0<= ix <= nx
            x = x0 + ix * dx
            print (t, x, u[ix], file=fall)
            print(t, x, u[ix], file=fone)
            print(t, x, u[ix], file=fevery)
    print(file=fevery)
    print(file=fall)
    print(t, (np.sum(u) - u[0]/2 - u[nx]/2) * dx, file=fenergy)
    for it in range(1, nt + 1): # 1 <= it <= nt
# ディリクレ境界条件
        for ix in range(1, nx): # 1 <= ix <= nx - 1
            du[ix] = coef * (u[ix + 1] + u[ix - 1] - 2.0 * u[ix])
        for ix in range(1, nx): # 1 <= ix <= nx - 1
            u[ix] += du[ix]
# ノイマン境界条件（コメントアウトにより保留）
#       du[0] = coef * (2.0 * u[1] - 2.0 * u[0])
#       for ix in range(1, nx): # 1 <= ix <= nx - 1
#           du[ix] = coef * (u[ix + 1] + u[ix - 1] - 2.0 * u[ix])
#       du[nx] = coef * (2.0 * u[nx - 1] - 2.0 * u[nx])
#       for ix in range(0, nx + 1): # 0 <= ix <= nx
#           u[ix] += du[ix]
        t += dt
        filename = "fdm1_{0:03d}.txt".format(it)
        with open(filename, "w") as fone:
            print(t, (np.sum(u) - u[0]/2 - u[nx]/2) * dx, \
                file=fenergy)
            for ix in range(0, nx + 1): # 0 <= ix <= nx
                x = x0 + ix * dx
                print(t, x, u[ix], file=fone)
                print(t, x, u[ix], file=fall)
                if it % 10 == 0:
                    print(t, x, u[ix], file=fevery)
        print(file=fall)
        if it % 10 == 0:
            print(file=fevery)
