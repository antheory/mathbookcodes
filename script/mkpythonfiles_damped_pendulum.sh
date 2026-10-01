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
# 減衰振り子の運動（2.2.2 減衰振り子の問題に現れる時間の定数，p.36）
EOF

################
# damped_pendulum.py

programname=damped_pendulum.py

echo "#" $programname $date > programhead.py
cat commentboundline.txt >> programhead.py
cat programtitle.txt >> programhead.py
cat bookinfo.txt >> programhead.py
cat commentboundline.txt >> programhead.py

cat programhead.py \
    $SRC/program2-1.py \
    $SRC/program2-2.py \
    $SRC/program2-3.py \
    $SRC/program2-4.py \
    $SRC/program2-5.py \
    $SRC/program2-6.py \
    $SRC/program2-7.py \
    > $programname

# 一時ファイルの消去
rm programhead.py
rm commentboundline.txt bookinfo.txt
rm programtitle.txt
