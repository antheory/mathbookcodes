# プログラム6-11（ストークスの公式で用いるphi(x)の奇関数の周期関数への拡張）
def u_init_odd(x):
    if x > 0.0:
        return u_init(x)
    else:
        return -u_init(-x)
def u_init_period(x):
    xtmp = x
    if xtmp > 0.0:
        while xtmp > l:
            xtmp -= 2.0 * l
    else:
        while xtmp < -l:
            xtmp += 2.0 * l
    return u_init_odd(xtmp)
