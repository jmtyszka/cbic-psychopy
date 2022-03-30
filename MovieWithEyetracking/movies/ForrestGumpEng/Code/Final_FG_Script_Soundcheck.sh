#!/bin/bash

cd /folder/containing/mp4/segment_0/of/ForrestGump

ffmpeg \
#or use fg_av_eng_seg0.mp4 for the English version
-i "fg_av_ger_seg0.mp4" \ 
-ss 00:03:10 \
-to 00:03:40 \
-map 0:v -map 0:a:0 \
-map_metadata -1 \
-vf scale=1280:-1 \
-c:a aac -vbr 5 \
-c:v libx264 -preset slow -crf 22 \
 -filter:v fps=30 \
-copyts \
-y \
"${FILE%.*}_soundcheck.mp4"
