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
# 熱伝導方程式の数値解（6.1.3 熱伝導・拡散方程式の解，p.173）
EOF
cat <<EOF > programsubtitle-fourier.txt
#  (1) フーリエの方法による計算
EOF
cat <<EOF > programsubtitle-fdm.txt
#  (2) 差分法を用いた解析
EOF
cat <<EOF > conditionb1.txt
#  境界条件1：ディリクレ境界条件
EOF
cat <<EOF > conditionb2.txt
#  境界条件2：ノイマン境界条件
EOF
cat <<EOF > conditioni1.txt
#  初期条件1：矩形波形
EOF
cat <<EOF > conditioni2.txt
#  初期条件2：正弦波形
EOF

# 準備
cat <<EOF > change6-7-bc1.sed
1s/.*/# プログラム6-7改（差分法の計算例）ディリクレ境界条件/
EOF
cat <<EOF > change6-7-bc2.sed
1s/.*/# プログラム6-7改（差分法の計算例）ノイマン境界条件/
21s/# ディリクレ境界条件/# ディリクレ境界条件（コメントアウトにより保留）/
22,25s/^ /#/
26s/# ノイマン境界条件（コメントアウトにより保留）/# ノイマン境界条件/
27,33s/^#/ /
EOF
cat <<EOF > pfourier-init.py
# 関連するモジュールのインポート
import numpy as np
import math
EOF
cat <<EOF > pfdm-init.py
# 関連するモジュールのインポート
import numpy as np
EOF

cat $SRC/program6-1.py >> pfourier-init.py
sed '1s/6-1/6-1改/;7,8d' $SRC/program6-1.py >> pfdm-init.py

cat $SRC/program6-2.py > pfourier-b1.py
cat $SRC/program6-3.py > pfourier-b2.py
cat $SRC/program6-4.py > pcommon-i1.py
cat $SRC/program6-5.py > pcommon-i2.py
cat $SRC/program6-6.py > pfourier-main.py

sed -f change6-7-bc1.sed $SRC/program6-7.py > pfdm-main-b1.py
sed -f change6-7-bc2.sed $SRC/program6-7.py > pfdm-main-b2.py

################
# heateq-fourier
for fnb in b1 b2
do
    for fni in i1 i2
    do
        programname=heateq-fourier-"$fnb"-"$fni".py
	echo "#" $programname $date > programhead.py
	cat commentboundline.txt >> programhead.py
	cat programtitle.txt >> programhead.py
        cat programsubtitle-fourier.txt >> programhead.py
	cat condition"$fnb".txt >> programhead.py
	cat condition"$fni".txt >> programhead.py
	cat bookinfo.txt >> programhead.py
	cat commentboundline.txt >> programhead.py
	cat programhead.py \
	    pfourier-init.py pfourier-"$fnb".py pcommon-"$fni".py \
	    pfourier-main.py > $programname
    done
done

################
# heateq-fdm
for fnb in b1 b2
do
    for fni in i1 i2
    do
	programname=heateq-fdm-"$fnb"-"$fni".py
	echo "#" $programname $date > programhead.py
	cat commentboundline.txt >> programhead.py
	cat programtitle.txt >> programhead.py
        cat programsubtitle-fdm.txt >> programhead.py
	cat condition"$fnb".txt >> programhead.py
	cat condition"$fni".txt >> programhead.py
	cat bookinfo.txt >> programhead.py
	cat commentboundline.txt >> programhead.py
	cat programhead.py \
	    pfdm-init.py pcommon-"$fni".py pfdm-main-"$fnb".py \
	    > $programname
  done
done

# 一時ファイルの消去
rm programhead.py
rm commentboundline.txt bookinfo.txt
rm programtitle.txt
rm programsubtitle-fourier.txt programsubtitle-fdm.txt
rm conditionb1.txt conditionb2.txt
rm conditioni1.txt conditioni2.txt
rm change6-7-bc1.sed change6-7-bc2.sed
rm pfourier-init.py pfdm-init.py pfourier-b1.py pfourier-b2.py
rm pcommon-i1.py pcommon-i2.py
rm pfourier-main.py
rm pfdm-main-b1.py pfdm-main-b2.py

