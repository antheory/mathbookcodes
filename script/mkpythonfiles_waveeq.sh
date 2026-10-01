#!/bin/sh

SRC="../src"

# date=`date`
date="2026/10/01"

cat <<EOF > commentboundline.txt
# --+----1----+----2----+----3----+----4----+----5----+----6----+----7--
EOF
cat <<EOF > bookinfo.txt
# 「機械工学のための数理モデリングと現象解析入門」
#   中谷彰宏著，2026年9月25日初版第1刷発行，コロナ社
#   (C) Akihiro Nakatani 2026
EOF

cat <<EOF > programtitle.txt
# 波動方程式の数値解（6.1.4 波動方程式の解，p.178）
EOF
cat <<EOF > programsubtitle-stokes.txt
#  (1) ストークスの公式の利用
EOF
cat <<EOF > programsubtitle-fourier.txt
#  (2) フーリエの方法
EOF
cat <<EOF > programsubtitle-fdm.txt
#  (3) 差分法
EOF

# 準備
cat <<EOF > pcommon0.py
# 関連するモジュールのインポート
import numpy as np
EOF

cat <<EOF > pmodule-fourier.py
import math
import scipy
from scipy import integrate
EOF

cat <<EOF > change6-8-fourier.sed
1s/# プログラム6-8/# プログラム6-8改/
EOF

cat <<EOF > add6-8-fourier.py
nmode = 100 # モード数
EOF

cat <<EOF > change6-9-stokes-fdm.sed
1s/# プログラム6-9/# プログラム6-9改/
3s/; An = np.zeros(nmode + 1)//
EOF

cat <<EOF > output-data.py
    filename = "wave_{0:03d}.txt".format(it) # 出力部
    with open(filename, "w") as fone:
        for ix in range(0, nx + 1): # 0 <= ix <= nx
            x = x0 + ix * dx
            print(t, x, u[ix], file=fone)
EOF

################
# wave-stokes.py
programname=wave-stokes.py

echo "#" $programname $date > programhead.py
cat commentboundline.txt >> programhead.py
cat programtitle.txt >> programhead.py
cat programsubtitle-stokes.txt >> programhead.py
cat bookinfo.txt >> programhead.py
cat commentboundline.txt >> programhead.py

cat pcommon0.py > tmp.py
cat $SRC/program6-8.py >> tmp.py
sed -f change6-9-stokes-fdm.sed $SRC/program6-9.py >> tmp.py

cat programhead.py \
    tmp.py \
    $SRC/program6-10.py \
    $SRC/program6-11.py \
    $SRC/program6-14.py \
    output-data.py \
    > $programname

################
# wave-fourier.py
programname=wave-fourier.py

echo "#" $programname $date > programhead.py
cat commentboundline.txt >> programhead.py
cat programtitle.txt >> programhead.py
cat programsubtitle-fourier.txt >> programhead.py
cat bookinfo.txt >> programhead.py
cat commentboundline.txt >> programhead.py

cat pcommon0.py pmodule-fourier.py > tmp.py
sed -f change6-8-fourier.sed $SRC/program6-8.py >> tmp.py
cat add6-8-fourier.py >> tmp.py
cat $SRC/program6-9.py >> tmp.py

cat programhead.py \
    tmp.py \
    $SRC/program6-10.py \
    $SRC/program6-12.py \
    $SRC/program6-13.py \
    $SRC/program6-15.py \
    output-data.py \
    > $programname

################
# wave-fdm.py
programname=wave-fdm.py

echo "#" $programname $date > programhead.py
cat commentboundline.txt >> programhead.py
cat programtitle.txt >> programhead.py
cat programsubtitle-fdm.txt >> programhead.py
cat bookinfo.txt >> programhead.py
cat commentboundline.txt >> programhead.py

cat pcommon0.py > tmp.py
cat $SRC/program6-8.py >> tmp.py
sed -f change6-9-stokes-fdm.sed $SRC/program6-9.py >> tmp.py

cat programhead.py \
    tmp.py \
    $SRC/program6-10.py \
    $SRC/program6-16.py \
    output-data.py \
    > $programname

# 一時ファイルの消去
rm programhead.py
rm commentboundline.txt bookinfo.txt
rm programtitle.txt
rm programsubtitle-stokes.txt
rm programsubtitle-fourier.txt
rm programsubtitle-fdm.txt
rm tmp.py
rm add6-8-fourier.py
rm change6-8-fourier.sed
rm change6-9-stokes-fdm.sed
rm output-data.py
rm pcommon0.py
rm pmodule-fourier.py
