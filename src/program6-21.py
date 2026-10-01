# プログラム6-21（ディリクレ境界の番号登録）
def setbound2():
    ibd = 0
    for ip in range(0, npoin):
        if i_bd[ip] != 0:
            i_bd[ip] = ibd + 1
            ip_bd[ibd] = ip
            ibd += 1
