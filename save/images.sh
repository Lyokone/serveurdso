#!/bin/bash


if [ $# -eq 0 ]; then
	echo "Need video as arg."
	exit 1
fi



vid=$1

mkdir images_$1
mv $vid images_$1/
cd images_$1

ffmpeg -i $vid -s $2 out%4d.jpg


#zip images_$1.zip *.jpg

#mv images_$1.zip ../
mv $vid ../
cd ../
#rm -r images_$1
