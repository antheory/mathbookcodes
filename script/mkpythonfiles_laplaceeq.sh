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
# ラプラス方程式の数値解（6.2.6 解法の適用と結果の可視化，p.189）
EOF
cat <<EOF > programsubtitle-fdm.txt
#  (1) 差分法（FDM）
EOF
cat <<EOF > programsubtitle-mc.txt
#  (2) モンテカルロ法（MC，ランダムウォーク）
EOF
cat <<EOF > programsubtitle-fem.txt
#  (3) 有限要素法（FEM）
EOF
cat <<EOF > programsubtitle-bem.txt
#  (4) 境界要素法（FDM）
EOF

# 準備
#$SRC/program6-17.py 共通
cat <<EOF > change6-17-fdm-mc-fem.sed
1s/# プログラム6-17/# プログラム6-17改/
3s/; DEBUG = False//
EOF
sed -f change6-17-fdm-mc-fem.sed < $SRC/program6-17.py > module-fdm-mc-fem.py
cat $SRC/program6-17.py > module-bem.py

#$SRC/program6-18.py 共通
cat $SRC/program6-18.py > dim-fdm-mc-fem-bem.py

#$SRC/program6-19.py bem 以外
cat <<EOF > change6-19-fdm.sed
1s/6-19（変数の定義など (BEM 以外，必要に応じて)）/6-19改（変数の定義など (FDM)）/
2d
3d
4d
6d
7s/総節点数 (FEM)，格子点数 (FDM, MC)/格子点数 (FDM)/
8d
9s/未知関数 (FEM，FDM, MC)/未知関数 (FDM)/
10d
11d
12s/設定（FDM, FEM, MC）/設定（FDM）/
EOF
sed -f change6-19-fdm.sed < $SRC/program6-19.py > params-fdm.py

cat <<EOF > change6-19-mc.sed
1s/6-19（変数の定義など (BEM 以外，必要に応じて)）/6-19改（変数の定義など (MC)）/
3d
6d
7s/総節点数 (FEM)，格子点数 (FDM, MC)/格子点数 (MC)/
8d
9s/未知関数 (FEM，FDM, MC)/未知関数 (MC)/
10d
11d
12s/設定（FDM, FEM, MC）/設定（MC）/
EOF
sed -f change6-19-mc.sed < $SRC/program6-19.py > params-mc.py

cat <<EOF > change6-19-fem.sed
1s/6-19（変数の定義など (BEM 以外，必要に応じて)）/6-19改（変数の定義など (FEM)）/
4d
7s/総節点数 (FEM)，格子点数 (FDM, MC)/総節点数 (FEM)/
9s/未知関数 (FEM，FDM, MC)/未知関数 (FEM)/
12s/設定（FDM, FEM, MC）/設定（FEM）/
EOF
sed -f change6-19-fem.sed < $SRC/program6-19.py > params-fem.py

#$SRC/program6-20.py bem 以外
cat <<EOF > change6-20-fdm-mc-fem.sed
1s/6-20（ディリクレ境界条件 (BEM 以外)）/6-20改（ディリクレ境界条件）/
EOF
sed -f change6-20-fdm-mc-fem.sed < $SRC/program6-20.py > boundary-fdm-mc-fem.py

#$SRC/program6-21.py bc
cat $SRC/program6-21.py > bound2-fdm-mc-fem.py

#$SRC/program6-22 FDM:main

#$SRC/program6-23 MC:randomwalk
#$SRC/program6-24 MC:main

#$SRC/program6-25 FEM:node
#$SRC/program6-26 FEM connectivity
#$SRC/program6-27 FEM:shape
#$SRC/program6-28 FEM: main

#$SRC/program6-29 FEM FDM output
cat <<EOF > change6-29-fdm.sed
1s/# プログラム6-29（解の出力(FEMの例，FDMも同様)）/# プログラム6-29改（解の出力(FDMの例)）/
2s/ffemall/ffdmall/
EOF
sed -f change6-29-fdm.sed < $SRC/program6-29.py > output-fdm.py

cat <<EOF > change6-29-fem.sed
1s/# プログラム6-29（解の出力(FEMの例，FDMも同様)）/# プログラム6-29改（解の出力(FEMの例)）/
EOF
sed -f change6-29-fem.sed < $SRC/program6-29.py > output-fem.py

#$SRC/program6-30 BEM 変数の宣言
#$SRC/program6-31 BEM ガウス積分の定数
#$SRC/program6-32 BEM 境界
#$SRC/program6-33 BEM 端点
#$SRC/program6-34 BEM 要素
#$SRC/program6-35 BEM 影響係数
#$SRC/program6-36 BEM 内点
#$SRC/program6-37 BEM メイン

################
# laplaceeq-fdm
programname=laplaceeq-fdm.py

echo "#" $programname $date > programhead.py
cat commentboundline.txt >> programhead.py
cat programtitle.txt >> programhead.py
cat programsubtitle-fdm.txt >> programhead.py
cat bookinfo.txt >> programhead.py
cat commentboundline.txt >> programhead.py

cat programhead.py \
    module-fdm-mc-fem.py \
    dim-fdm-mc-fem-bem.py \
    params-fdm.py \
    boundary-fdm-mc-fem.py \
    bound2-fdm-mc-fem.py \
    $SRC/program6-22.py \
    output-fdm.py \
    > $programname

################
# laplaceeq-mc
programname=laplaceeq-mc.py

echo "#" $programname $date > programhead.py
cat commentboundline.txt >> programhead.py
cat programtitle.txt >> programhead.py
cat programsubtitle-mc.txt >> programhead.py
cat bookinfo.txt >> programhead.py
cat commentboundline.txt >> programhead.py

cat programhead.py \
    module-fdm-mc-fem.py \
    dim-fdm-mc-fem-bem.py \
    params-mc.py \
    boundary-fdm-mc-fem.py \
    bound2-fdm-mc-fem.py \
    $SRC/program6-23.py \
    $SRC/program6-24.py \
    > $programname

################
# laplaceeq-fem
programname=laplaceeq-fem.py

echo "#" $programname $date > programhead.py
cat commentboundline.txt >> programhead.py
cat programtitle.txt >> programhead.py
cat programsubtitle-fem.txt >> programhead.py
cat bookinfo.txt >> programhead.py
cat commentboundline.txt >> programhead.py

cat programhead.py \
    module-fdm-mc-fem.py \
    dim-fdm-mc-fem-bem.py \
    params-fem.py \
    boundary-fdm-mc-fem.py \
    bound2-fdm-mc-fem.py \
    $SRC/program6-25.py \
    $SRC/program6-26.py \
    $SRC/program6-27.py \
    $SRC/program6-28.py \
    output-fem.py \
    > $programname

################
# laplaceeq-bem
programname=laplaceeq-bem.py

echo "#" $programname $date > programhead.py
cat commentboundline.txt >> programhead.py
cat programtitle.txt >> programhead.py
cat programsubtitle-bem.txt >> programhead.py
cat bookinfo.txt >> programhead.py
cat commentboundline.txt >> programhead.py

cat programhead.py \
    module-bem.py \
    dim-fdm-mc-fem-bem.py \
    $SRC/program6-30.py \
    $SRC/program6-31.py \
    $SRC/program6-32.py \
    $SRC/program6-33.py \
    $SRC/program6-34.py \
    $SRC/program6-35.py \
    $SRC/program6-36.py \
    $SRC/program6-37.py \
    > $programname

# 一時ファイルの消去
rm programhead.py
rm commentboundline.txt bookinfo.txt
rm programtitle.txt
rm programsubtitle-bem.txt
rm programsubtitle-fdm.txt
rm programsubtitle-fem.txt
rm programsubtitle-mc.txt
rm bound2-fdm-mc-fem.py
rm boundary-fdm-mc-fem.py
rm change6-17-fdm-mc-fem.sed
rm change6-19-fdm.sed change6-19-fem.sed change6-19-mc.sed
rm change6-20-fdm-mc-fem.sed
rm change6-29-fdm.sed change6-29-fem.sed
rm dim-fdm-mc-fem-bem.py
rm module-bem.py module-fdm-mc-fem.py
rm output-fdm.py output-fem.py
rm params-fdm.py params-fem.py params-mc.py
