#!/bin/bash

cd /folder/containing/mkv/segments/of/ForrestGump

for FILE in *.mkv; do
  ffmpeg \
  -i "$FILE" \
  -map 0:v -map 0:a:0 \
  -map_metadata -1 \
  -vf scale=1280:-1 \
  -c:a aac -vbr 5 \
  -c:v libx264 -preset slow -crf 22 \
  -filter:v fps=30 \
  -copyts \
  -y \
  "${FILE%.*}.mp4"
done 
