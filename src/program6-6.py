# プログラム6-6（フーリエの方法の計算例）
An = np.zeros(nmode + 1)
for imode in range(imode_ini, nmode + 1):
    An[imode] = A_fourier(imode)
t = 0.0
for imode in range(imode_ini, nmode + 1):
    filename = "fmode1_{0:03d}.txt".format(imode)
    with open(filename, "w") as fmode:
        for ix in range(0, nx + 1): # 0 <= ix <= nx
            x = x0 + ix * dx
            print(t, x, u_phin(x, t, imode), file=fmode)
u = np.zeros(nx +1)
with open("fourier1.txt", "w") as fall, \
     open("fourier1_energy.txt", "w") as fenergy, \
     open("fourier1_every.txt", "w") as fevery:
    for it in range(0, nt + 1): # 0<= it <= nt
        t = t0 + it * dt
        for ix in range(0, nx + 1): # 0 <= ix <= nx
            x = x0 + ix * dx
            u[ix] = 0.0
            for imode in range(imode_ini, nmode + 1):
                u[ix] += u_phin(x, t, imode)
        filename = "fourier1_{0:03d}.txt".format(it)
        with open(filename, "w") as fone:
            energy = (np.sum(u) - u[0] / 2.0 - u[nx] / 2.0) * dx
            print(t, energy, file=fenergy)
            for ix in range(0, nx + 1): # 0 <= ix <= nx
                x = x0 + ix * dx
                print(t, x, u[ix], file=fone)
                print(t, x, u[ix], file=fall)
                if it % 10 == 0:
                    print(t, x, u[ix], file=fevery)
        print(file=fall)
        if it % 10 == 0:
            print(file=fevery)
