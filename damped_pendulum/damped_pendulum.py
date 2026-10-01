# damped_pendulum.py 2026/10/01
# --+----1----+----2----+----3----+----4----+----5----+----6----+----7--
# 減衰振り子の運動（2.2.2 減衰振り子の問題に現れる時間の定数，p.36）
# 「機械工学のための数理モデリングと現象解析入門」
#   中谷彰宏著，2026年9月25日初版第1刷発行，コロナ社
#   (C) Akihiro Nakatani 2026
# --+----1----+----2----+----3----+----4----+----5----+----6----+----7--
# プログラム2-1（関連するモジュールのインポート）
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import math
import tkinter as tk
from tkinter import messagebox
# プログラム2-2（定数の定義）
g_over_l = 1.0; theta_0 = 0.0
# プログラム2-3（入力ウインドウの定義）
root = tk.Tk()
root.title("Parameters")
root.geometry("360x120")
input_valone_label = tk.Label(text="c/m")
input_valone_label.grid(row=1, column=1, padx=10)
input_valone = tk.Entry(width=40)
input_valone.grid(row=1, column=2)
input_valtwo_label = tk.Label(text="w0")
input_valtwo_label.grid(row=2, column=1, padx=10)
input_valtwo = tk.Entry(width=40)
input_valtwo.grid(row=2, column=2)
# プログラム2-4（運動方程式の記述）
def funcdxdt(t, x, g_over_l, c_over_m):
    dxdt = np.zeros(2)
    dxdt[0] = x[1]
    dxdt[1] = -g_over_l * math.sin(x[0]) - c_over_m * x[1]
    return dxdt
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
# プログラム2-7（入力ウインドウの操作）
def button_click():
    try:
        c_over_m = float(input_valone.get())
        omega_0 = float(input_valtwo.get())
    except ValueError:
        messagebox.showerror(
            "Input error", "Please enter valid numbers."
        )
        return
    mymain(c_over_m, omega_0)
    myplotgraph(c_over_m, omega_0)
def button_quit():
    root.destroy()
    plt.close("all")
button1 = tk.Button(root, text="ENTER", command=button_click)
button1.place(x=10, y=80)
button2 = tk.Button(root, text="Quit", command=button_quit)
button2.place(x=100, y=80)
root.mainloop()
