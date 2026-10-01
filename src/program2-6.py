# プログラム2-6（グラフ表示）
def myplotgraph(c_over_m, omega_0):    
    gx=[]; gy=[]
    with open("output.txt", "rt") as fall:
        for line in fall:
            data = line.split()
            gx.append(float(data[0]))
            gy.append(float(data[1]))
    plt.figure()
    plt.plot(gx, gy)
    plt.xlabel(r"$t$")
    plt.ylabel(r"$\theta$")
    gtitle = "$c/m$:" + str(c_over_m) + ", "
    gtitle += r"$\omega_0$:" + str(omega_0)
    plt.title(gtitle, loc="center")
    plt.grid(True)
    plt.show()
