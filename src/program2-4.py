# プログラム2-4（運動方程式の記述）
def funcdxdt(t, x, g_over_l, c_over_m):
    dxdt = np.zeros(2)
    dxdt[0] = x[1]
    dxdt[1] = -g_over_l * math.sin(x[0]) - c_over_m * x[1]
    return dxdt
