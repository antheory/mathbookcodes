# プログラム6-12（フーリエの方法で用いるフーリエ係数の計算）
def A_integrand(x, n):
    k = n * math.pi / l
    return u_init(x) * math.sin(k * x)
def A_fourier(n):
    val, _ = scipy.integrate.quad(A_integrand, x0, x1, args=(n))
    val *= 2 / l
    return val
for imode in range(1, nmode + 1): # 1 <= imode <= nmode
    An[imode] = A_fourier(imode)
