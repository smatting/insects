#!/bin/bash

var=0

for f in 01original/*.jpg; do
    f="$(basename -- $f)"
    echo $var, $f
    num=$(printf "%05d" $var)
    
    cp 01original/${f} 04prepareddata/images/coift_${num}.jpg
    cp 03boundingboxes/${f%.jpg}.txt 04prepareddata/annotations/coift_${num}.txt

    var=$((var + 1))
done