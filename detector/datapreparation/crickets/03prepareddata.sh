#!/bin/bash

var=0

for f in 02annotations/*; do
    f="$(basename -- $f)"
    echo $var, $f
    num=$(printf "%05d" $var)
    
    cp 00original/${f%.txt}.jpg 03prepareddata/images/
    cp 02annotations/${f} 03prepareddata/images/

    var=$((var + 1))
done