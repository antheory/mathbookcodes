# プログラム6-2（境界条件1: ディリクレ問題の場合）
imode_ini = 1
def A_integrand(x, n):
    k = n * math.pi / l
    return u_init(x) * math.sin(k * x)
def A_fourier(n):
    val, _ = scipy.integrate.quad(A_integrand, x0, x1, args=(n,))
    val *= 2 / l
    return val
def u_phin(x, t, n):
    k = n * math.pi / l
    return An[n] * math.exp(- ckappa * k**2 * t) * math.sin(k * x)
