#!/bin/bash

if [ $# -eq 0 ]; then
	echo "Need folder as argument."
	exit 1
fi

FILE=$1
PHONE=$2

./dso_dataset files=$FILE calib=../../phone_calib/$2 preset=0 mode=1 nogui=1 nolog=1 sampleoutput=1 quiet=1
        
echo ''


# gamma="$FILE/pcalib.txt" vignette="$FILE/vignette.png" \
