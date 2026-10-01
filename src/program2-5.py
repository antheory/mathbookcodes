# プログラム2-5（メイン計算）
def mymain(c_over_m, omega_0):
    t0 = 0.0; t1 = 100.0; n = 1000
    t = np.linspace(t0, t1, num=n + 1)
    x0 = (theta_0, omega_0) # 初期条件
    sol = solve_ivp(funcdxdt, (t0, t1), x0, method="RK45", \
         t_eval=t, args=(g_over_l, c_over_m),)
    allsol = np.vstack((sol.t, sol.y)).T # theta と omega を同時に
    with open("output.txt", "w") as fall:
        for i in range(len(allsol)):
            print (allsol[i][0], allsol[i][1], allsol[i][2], \
                file=fall)
