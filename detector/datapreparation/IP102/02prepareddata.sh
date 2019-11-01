#!/bin/bash

var=0

for f in 01boundingboxes/*; do
    f="$(basename -- $f)"
    echo $var, $f
    num=$(printf "%05d" $var)
    
    cp 00original/JPEGImages/${f%.txt}.jpg 02prepareddata/images/ip120_${num}.jpg
    cp 01boundingboxes/${f} 02prepareddata/annotations/ip120_${num}.txt

    var=$((var + 1))
done