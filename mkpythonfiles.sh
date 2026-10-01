#!/bin/sh

scriptdir=script

for i in damped_pendulum heateq waveeq laplaceeq
do
  if [ ! -e $i ]; then
    mkdir $i
  fi
  cd $i
  ls
  sh ../$scriptdir/mkpythonfiles_"$i".sh
  cd ..
done
