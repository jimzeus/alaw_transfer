#!/usr/bin/env sh
if [ $# -ne 2 ] || [ ! -f $1 ]; 
then
	echo "Usage:"
	echo "   "$0" VIDEO_FILE WAVE_FILE"
	echo "Description:"
	echo "   extract audio from VIDEO_FILE to WAVE_FILE(.wav)"
	exit
else
	ffmpeg -i $1 -ab 160k -ac 1 -ar 8000 -vn $2
fi
