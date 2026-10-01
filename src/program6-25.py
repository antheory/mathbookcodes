# プログラム6-25（FEM:節点の生成）
def setnode():
     ip = 0
     for iy in range(0, ny + 1):
          for ix in range(0, nx + 1):
               xp[ip][0] = x0 + ix * dx
               xp[ip][1] = y0 + iy * dy
               ip += 1
