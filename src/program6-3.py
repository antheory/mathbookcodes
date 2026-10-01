# プログラム6-3（境界条件2: ノイマン問題の場合）
imode_ini = 0
def A_integrand(x, n):
    k = n * math.pi / l
    return u_init(x) * math.cos(k * x)
def A_fourier(n):
    val, _ = scipy.integrate.quad(A_integrand, x0, x1, args=(n,))
    if n == 0:
        val *= 1 / l
    else:
        val *= 2 / l
    return val
def u_phin(x, t, n):
    k = n * math.pi / l
    return An[n] * math.exp(- ckappa * k**2 * t) * math.cos(k * x)
