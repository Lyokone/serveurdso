#!/bin/bash

search=""

while [ $# -gt 0 ]; do

	case $1 in
		("make")
			echo "Compiling."
			g++ -c camera_calibration.cpp -Wall `pkg-config opencv --cflags`
			g++ camera_calibration.o -o calib `pkg-config opencv --libs`

			echo "Cleaning."
			rm camera_calibration.o;;
	
		("resize")
			echo "Resising requires imagemagick."

			echo $1 $2
			if [ $# -eq 1 ]; then
				echo "Requires dimension in format WxH. Add ! to ignore ratio."
				exit 1
			fi
			cd $path
			for f in *.jpg; do
				convert -resize $2 $f $f
			done
			echo -e "Done resizing images.\n\n"
			cd ..
			shift;;
			
		("search")
			echo "Will search for best board size."
			search="search";;
		
		("video")
			if [ $# -eq 1 ]; then
				echo "Requires video file."
				exit 1
			fi
			path=$3
			echo "Converting video into images with fps : 0.5"
			ffmpeg -i $2 -vf fps=0.5 $path/out%3d.jpg
			echo -e "Done converting video.\n\n"
			shift 2;;
			
		(*)
			echo "Unknown command $1 ." 
			echo "Usage :"
			echo -e "\tmake :\t\tForce compilation."
			echo -e "\tresize :\tResize jpg in images folder. Requires dimension in format WxH. Add ! to ignore ratio."
			echo -e "\tsearch :\tSearch for best boardSize."
			exit 1;;
			
			
	esac
	shift
done

if ! [ -f calib ]; then
	echo "Compiling."
	g++ -c camera_calibration.cpp -Wall `pkg-config opencv --cflags`
	g++ camera_calibration.o -o calib `pkg-config opencv --libs`

	echo "Cleaning."
	rm camera_calibration.o
fi

cd $path

pwd

echo '<?xml version="1.0"?>
<opencv_storage>
<images>'>images.xml

i=0
for f in *.jpg; do
	echo "$path/$f">>images.xml
	i=$(expr $i + 1)
done;
echo "</images>
<Number>$i</Number>
</opencv_storage>">>images.xml

cd ..

xmlstarlet edit -L -u "opencv_storage/Settings/Input" -v $path/images.xml default.xml

echo "Starting calibration."
./calib $search
echo -e "\nDone."
