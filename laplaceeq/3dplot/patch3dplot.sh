#!/bin/sh

# prepare patch files
# laplaceeq-bem-3dplot.patch
# laplaceeq-fdm-3dplot.patch
# laplaceeq-fem-3dplot.patch
# laplaceeq-mc-3dplot.patch

for i in bem fdm fem mc 
do
  cp -p ../laplaceeq-"$i".py ./laplaceeq-"$i"-3dplot.py
  patch < laplaceeq-"$i"-3dplot.patch ./laplaceeq-"$i"-3dplot.py
done
