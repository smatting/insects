#!/bin/bash

var=0

for d in 00original/JPEG_lowRes/*; do
    echo $d
    for s in set0 set1 set2; do
        echo $s
        for f in ${d}/${s}/*.jpg; do

            f="$(basename -- $f)"
            echo $var, $f
            num=$(printf "%05d" $var)
            
            cp ${d}/${s}/${f} 02prepareddata/images/stonefly9_${num}.jpg
            cp 01boundingboxes/${f%.jpg}.txt 02prepareddata/annotations/stonefly9_${num}.txt

            var=$((var + 1))
        done
    done
done